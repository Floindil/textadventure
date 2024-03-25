import pygame

class UIElement:

    TAG = "UIElement"
    _display_surface: pygame.Surface
    position = pygame.Vector2
    rect = pygame.Rect
    surface = pygame.Surface
    _text: pygame.Surface

    def __init__(self,
            _display_surface: pygame.Surface,
            position: tuple,
            size: tuple,
            text: str = ""
        ):
        self._display_surface = _display_surface
        self.position = pygame.Vector2(position)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.surface = pygame.Surface(size)
        self._text = text
        if text:
            font = pygame.font.Font("app/src/assets/fonts/Montserrat-Black.ttf", 20)
            _text = font.render(text, True, "Black")
            self._text = _text

    def mousecheck(self) -> bool:
        _mousecoordinates = pygame.Vector2(pygame.mouse.get_pos())
        return self.rect.collidepoint(_mousecoordinates.x, _mousecoordinates.y)
    
    def render(self):
        self._display_surface.blit(self.surface, self.position.xy)
    
    def update(self):
        pass
    
    def load_image(self, image_path: str):
        self.surface = pygame.image.load(image_path)
        self._add_text()

    def fill(self, color: str):
        self.surface.fill(color)
        self._add_text()

    def _add_text(self):
        if self._text:
            self.surface.blit(self._text, pygame.Vector2(self.rect.size)/2-pygame.Vector2(self._text.get_size())/2)

    def action(self):
        pass

class Button(UIElement):

    TAG = "Button"
    _command: callable

    def __init__(self,
            _display_surface: pygame.Surface,
            position: tuple,
            size: tuple,
            command: callable,
            text: str = ""
        ):
        super().__init__(_display_surface, position, size, text)
        self._command = command

    def action(self):
        if self.mousecheck():
            self._command()

    def change_command(self, new_command: callable):
        self._command = new_command

class DropZone(UIElement):

    TAG = "DropZone"

    def __init__(self,
            _display_surface: pygame.Surface,
            position: tuple,
            size: tuple,
        ):
        super().__init__(_display_surface, position, size)

class Movable(UIElement):

    TAG = "Movable"
    draw_position: pygame.Vector2
    grabbed: bool
    active_zone: DropZone
    registered_zones: list[DropZone]

    def __init__(self, _display_surface: pygame.Surface, position: tuple, size: tuple, text: str = ""):
        super().__init__(_display_surface, position, size, text)
        self.draw_position = position
        self.grabbed = False
        self.active_zone = None
        self.registered_zones = []

    def action(self):
        print(self.grabbed)
        if self.mousecheck():
            self.grabbed = True

    def drop(self):
        mouse_pos = pygame.mouse.get_pos()
        for zone in self.registered_zones:
            if zone.rect.collidepoint(mouse_pos):
                self.set_zone(zone)
            else:
                self.draw_position = self.position
        self.grabbed = False

    def set_zone(self, zone: DropZone):
        self.active_zone = zone
        self.update_pos(zone.rect.center-pygame.Vector2(self.rect.size)/2)
        self.update_draw_pos()

    def register_zone(self, zone: DropZone):
        self.registered_zones.append(zone)

    def update(self):
        if self.grabbed:
            mouse_pos = pygame.mouse.get_pos()
            self.draw_position = mouse_pos - pygame.Vector2(self.rect.size)/2

    def update_draw_pos(self, position: pygame.Vector2 = None):
        if position:
            self.draw_position = position
        else:
            self.draw_position = self.position

    def update_pos(self, position: pygame.Vector2):
        self.position = position
        self.rect.topleft = position

    def render(self):
        self._display_surface.blit(self.surface, self.draw_position)
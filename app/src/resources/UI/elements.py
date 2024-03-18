import pygame

class UIElements:

    TAG = "UIElement"

    def __init__(self,
        display_surface: pygame.surface.Surface,
        display_position: tuple,
        size: tuple
        ):
        self._display_surface = display_surface
        self._display_position = display_position
        self._rect = pygame.Rect(display_position[0], display_position[1], size[0], size[1])
        self.surface = pygame.Surface(size)

    def mousecheck(self) -> bool:
        _mousecoordinates = pygame.Vector2(pygame.mouse.get_pos())
        return self._rect.collidepoint(_mousecoordinates.x, _mousecoordinates.y)
    
    def place(self):
        self._display_surface.blit(self.surface, self._rect.topleft)

class Button(UIElements):

    TAG = "Button"

    def __init__(self, display_surface: pygame.Surface, display_position: tuple, size: tuple, command: callable, text: str = ""):
        super().__init__(display_surface, display_position, size)
        self.pressed = False
        self._command = command
        self._text = text
        if text:
            font = pygame.font.Font("app/src/assets/fonts/Montserrat-Black.ttf", 20)
            _text = font.render(text, True, "Black")
            self._text = _text

    def action(self):
        self._command()

    def change_command(self, new_command: callable):
        self._command = new_command

    def load_image(self, image_path: str):
        _image = pygame.image.load(image_path)
        self.surface.blit(_image)
        self._add_text()

    def fill(self, color: str):
        self.surface.fill(color)
        self._add_text()

    def _add_text(self):
        if self._text:
            self.surface.blit(self._text, pygame.Vector2(self._rect.size)/2-pygame.Vector2(self._text.get_size())/2)
import pygame

class UIElements:
    def __init__(self,
        display_surface: pygame.surface.Surface,
        display_position: tuple,
        size: tuple
        ):
        self._display_surface = display_surface
        self._display_position = display_position
        self._rect = pygame.Rect(display_position[0], display_position[1], size[0], size[1])

    def mousecheck(self) -> bool:
        _mousecoordinates = pygame.Vector2(pygame.mouse.get_pos())
        return self._rect.collidepoint(_mousecoordinates.x, _mousecoordinates.y)
    
    def place(self):
        self._display_surface.blit(self._surface, self._rect.topleft)

class Button(UIElements):
    def __init__(self, display_surface: pygame.Surface, display_position: tuple, size: tuple, command: callable):
        super().__init__(display_surface, display_position, size)
        self._surface = pygame.Surface(size)
        self.pressed = False
        self._command = command

    def action(self):
        self._command()

    def load_image(self, image_path: str):
        _image = pygame.image.load(image_path)
        self._surface.blit(_image)

    def fill(self, color: str):
        self._surface.fill(color)
import pygame

class Entity:

    _display_surface: pygame.Surface
    position: pygame.Vector3
    surface: pygame.Surface
    rect: pygame.Rect

    def __init__(self,
            _display_surface: pygame.Surface,
            texture: pygame.Surface,
            position: pygame.Vector3
        ) -> None:
        self._display_surface = _display_surface
        self.surface = texture
        self.rect = texture.get_rect()
        self.position = position

    def update(self, new_position: pygame.Vector3):
        self.position = new_position
        self.rect.left = self.position.x
        self.rect.top = self.position.y

    def render(self):
        self._display_surface.blit(self.surface, self.position.xy)
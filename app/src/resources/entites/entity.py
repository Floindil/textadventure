import pygame

class Entity:

    position: pygame.Vector3
    surface: pygame.Surface
    rect: pygame.Rect

    def __init__(self, texture: pygame.Surface, position: pygame.Vector3) -> None:
        self.surface = texture
        self.rect = texture.get_rect()
        self.position = position

    def update(self, new_position):
        self.position = new_position
        self.rect.left = self.position.x
        self.rect.top = self.position.y
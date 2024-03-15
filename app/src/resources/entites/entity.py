import pygame

class Entity:
    position: pygame.Vector3
    surface: pygame.Surface
    def __init__(self, texture: pygame.Surface, position: pygame.Vector3) -> None:
        self.surface = texture
        self.position = position

    def update(self, new_position):
        self.position = new_position
import pygame
from src.resources.entites.entity import Entity

class Map3D:

    texture: pygame.image
    rect: pygame.Rect
    bounds: pygame.Rect
    colliders: list[pygame.Rect]

    def __init__(self, display_surface: pygame.Surface, image_path: str) -> None:
        self._display_surface = display_surface
        self.texture = pygame.image.load(image_path)
        self.rect = self.texture.get_rect()
        self.colliders = []

    def add_bounds(self, player: Entity) -> pygame.Rect|None:
            self.bounds = pygame.Rect(
                player.rect.right,
                player.rect.bottom,
                self.rect.right - 2*player.rect.right,
                self.rect.height - 2*player.rect.height
            )
    
    def add_collider(self, collider: pygame.Rect):
        self.colliders.append(collider)

    def new_collider(self, size: tuple, topleft: tuple):
        self.add_collider(pygame.Rect(topleft[0], topleft[1], size[0], size[1]))

    def render(self):
        self._display_surface.blit(self.texture,(0,0))
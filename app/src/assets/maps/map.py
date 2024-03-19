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

    def add_bounds(self, player: Entity) -> pygame.Rect:
            if player:
                self.bounds = pygame.Rect(
                    player.rect.right-1,
                    player.rect.bottom-1,
                    self.rect.right + 1 - 2*player.rect.right,
                    self.rect.height + 1 - 2*player.rect.height
                )
            else:
                 self.bounds = self.rect
    
    def add_collider(self, collider: pygame.Rect):
        self.colliders.append(collider)

    def new_collider(self, size: tuple, topleft: tuple):
        self.add_collider(pygame.Rect(topleft[0], topleft[1], size[0], size[1]))

    def render(self):
        self._display_surface.blit(self.texture,(0,0))
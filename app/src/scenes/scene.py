import pygame
from src.assets.maps.map import Map3D
from src.resources.ui.elements import Button
from src.resources.entites.entity import Entity

class Scene:
    _display_surface: pygame.Surface
    surface: pygame.Surface
    buttons: list[Button]
    entities: list[Entity]
    player: Entity
    map3d = Map3D

    def __init__(self, _display_surface: pygame.Surface) -> None:
        self._display_surface = _display_surface
        self.surface = pygame.Surface(_display_surface.get_size())
        self.map3d = pygame.Surface(_display_surface.get_size())
        self.buttons = []
        self.entities = []

    def render(self):
        self.surface.blit(self.map3d.texture,(0,0))
        for button in self.buttons:
            button.place()
        for entity in self.entities:
            self.surface.blit(entity.surface, (entity.position.x, entity.position.y))

        '''###### DEBUG
        pygame.draw.rect(self.surface, "green", self.map3d.bounds)
        if self.player:
            pygame.draw.rect(self.surface, "blue", self.player.rect)
        for collider in self.map3d.colliders:
            pygame.draw.rect(self.surface,"red", collider)
        ###### DEBUG'''
        
        self._display_surface.blit(self.surface, self._display_surface.get_rect().topleft)

    def add_button(self, button: Button):
        self.buttons.append(button)

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def check_colliders(self, entity: Entity) -> bool:
        for collider in self.map3d.colliders:
            if collider.colliderect(entity.rect):
                return True
    
    def check_bounds(self, entity: Entity) -> bool:
        return self.map3d.bounds.colliderect(entity.rect)
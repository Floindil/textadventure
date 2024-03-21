import pygame
from src.assets.maps.map import Map3D
from src.resources.ui.elements import Button, UIElement
from src.resources.ui.controller import Controller
from src.resources.entites.entity import Entity

class Scene:

    _display_surface: pygame.Surface
    surface: pygame.Surface
    buttons: list[Button]
    to_display: list[Entity|UIElement]
    player: Entity
    map3d = Map3D

    def __init__(self, _display_surface: pygame.Surface) -> None:
        self._display_surface = _display_surface
        self.surface = pygame.Surface(_display_surface.get_size())
        self.map3d = pygame.Surface(_display_surface.get_size())
        self.buttons = []
        self.to_display = []

    def render(self):
        self.surface.blit(self.map3d.texture,(0,0))
        
        for entity in self.to_display:
            self.surface.blit(entity.surface, (entity.position.x, entity.position.y))
        
        self._display_surface.blit(self.surface, self._display_surface.get_rect().topleft)

    def add_button(self, button: Button):
        self.buttons.append(button)
        self.to_display.append(button)

    
    def add_controller(self, controller: Controller):
        self.controller = controller

    def add_to_display(self, entity: Entity):
        self.to_display.append(entity)

    def check_colliders(self, entity: Entity) -> bool:
        for collider in self.map3d.colliders:
            if collider.colliderect(entity.rect):
                return True
    
    def check_bounds(self, entity: Entity) -> bool:
        return self.map3d.bounds.colliderect(entity.rect)
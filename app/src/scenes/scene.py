import pygame
from src.resources.ui.elements import Button
from src.resources.entites.entity import Entity

class Scene:
    _display_surface: pygame.Surface
    surface: pygame.Surface
    buttons: list[Button]
    entities: list[Entity]

    def __init__(self, _display_surface: pygame.Surface) -> None:
        self._display_surface = _display_surface
        self.surface = pygame.Surface(_display_surface.get_size())
        self.background = pygame.Surface(_display_surface.get_size())
        self.buttons = []
        self.entities = []

    def render(self):
        self.surface.blit(self.background,(0,0))
        for button in self.buttons:
            button.place()
        for entity in self.entities:
            self.surface.blit(entity.surface, (entity.position.x, entity.position.y))
        self._display_surface.blit(self.surface, self._display_surface.get_rect().topleft)

    def add_button(self, button: Button):
        self.buttons.append(button)

    def add_entity(self, entity: Entity):
        self.entities.append(entity)
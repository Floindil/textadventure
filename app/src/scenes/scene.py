import pygame
from src.resources.UI.elements import Button

class Scene:
    _display_surface: pygame.Surface
    surface: pygame.Surface
    buttons: list[Button]

    def __init__(self, _display_surface: pygame.Surface) -> None:
        self._display_surface = _display_surface
        self.surface = pygame.Surface(_display_surface.get_size())
        self.buttons = []

    def render(self):
        self._display_surface.blit(self.surface, self._display_surface.get_rect().topleft)
        for button in self.buttons:
            button.place()

    def add_button(self, button: Button):
        self.buttons.append(button)
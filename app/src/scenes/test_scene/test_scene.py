import pygame
from src.scenes.scene import Scene
from src.resources.UI.elements import Button

class TestScene(Scene):
    def __init__(self, _display_surface: pygame.Surface) -> None:
        super().__init__(_display_surface)
        self.surface.fill("blue")

    def some_action(self):
        print("action!")
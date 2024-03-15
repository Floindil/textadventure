import pygame
from src.scenes.scene import Scene
from src.resources.ui.elements import Button
from src.resources.entites.entity import Entity
from src.resources.ui.controller import Controller

class TestScene(Scene):
    def __init__(self, _display_surface: pygame.Surface) -> None:
        super().__init__(_display_surface)
        self.surface.fill("blue")
        self.controller = None

        player_surface = pygame.Surface((50,50))
        pygame.draw.circle(player_surface,"red",(25,25),25)
        player_start = pygame.Vector3(200,200,0)
        self.player = Entity(player_surface, player_start)
        self.add_entity(self.player)

    def some_action(self):
        print("action!")

    def add_controller(self, controller: Controller):
        self.controller = controller
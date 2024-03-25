import pygame
from src.scenes.scene import Scene
from src.resources.ui.elements import Button
from src.assets.maps.map import Map3D
from src.resources.entites.entity import Entity

class TestScene(Scene):

    map3d: Map3D
    player: Entity

    def __init__(self, _display_surface: pygame.Surface) -> None:
        super().__init__(_display_surface, True)

        player_surface = pygame.image.load("app/src/red_circle.png")
        player_start = pygame.Vector3(200,200,0)
        self.player = Entity(self.surface, player_surface, player_start)
        self.add_to_display(self.player)

        self.map3d = Map3D(_display_surface, "app/src/assets/maps/testmap.png")
        self.map3d.add_bounds(self.player)
        self.map3d.new_collider((125,80),(55,50))
        self.map3d.new_collider((200,141),(80,375))

    def some_action(self):
        print("action!")
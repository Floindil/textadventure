import pygame
from src.scenes.scene import Scene
from src.assets.maps.map import Map3D
from src.resources.ui.elements import Button
from src.resources.entites.entity import Entity

class Inventory(Scene):

    map3d: Map3D

    def __init__(self, _display_surface: pygame.Surface) -> None:
        super().__init__(_display_surface)
        self.map3d = Map3D(_display_surface, "app/src/assets/maps/menu.png")
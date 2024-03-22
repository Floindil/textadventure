import pygame
from src.scenes.scene import Scene
from src.assets.maps.map import Map3D
from src.resources.ui.elements import Button
from src.resources.entites.entity import Entity

class Menu(Scene):

    map3d: Map3D
    player: Entity

    def __init__(self, _display_surface: pygame.Surface) -> None:
        super().__init__(_display_surface)
        self.map3d = Map3D(_display_surface, "app/src/assets/maps/menu.png")

        buttonsize = (200,30)
        displaySize = self.surface.get_size()
        buttonposition = (displaySize[0]/2-buttonsize[0]/2,displaySize[1]/2-buttonsize[1]/2)
        button = Button((buttonposition), buttonsize, self.some_action, "ACTION")
        button.fill("white")
        self.add_button(button)
    
    @staticmethod
    def some_action():
        print("action")

import pygame
from src.scenes.scene import Scene
from src.assets.maps.map import Map3D
from src.resources.ui.elements import Button, DropZone, Movable
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
        button = Button(self.surface, (buttonposition), buttonsize, self.some_action, "ACTION")
        button.fill("white")
        self.add_ui_element(button)

        zone1 = DropZone(self.surface, (100,100), (100,100))
        zone1.fill("green")
        zone2 = DropZone(self.surface, (100,250), (100,100))
        zone2.fill("blue")

        movable_img = pygame.image.load("app/src/red_circle.png")
        movable = Movable(self.surface, (100,100), movable_img.get_size())
        movable.load_image("app/src/red_circle.png")

        movable.set_zone(zone1)
        movable.register_zone(zone2)
        movable.register_zone(zone1)

        self.add_ui_element(zone1)
        self.add_ui_element(zone2)
        self.add_ui_element(movable)
    
    @staticmethod
    def some_action():
        print("action")

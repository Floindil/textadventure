import pygame
from src.scenes.scene import Scene
from src.assets.maps.map import Map3D
from src.resources.ui.elements import Button, DropZone, Movable
from src.resources.entites.entity import Entity

class Inventory(Scene):

    def __init__(self, _display_surface: pygame.Surface) -> None:
        super().__init__(_display_surface)
        self.surface.fill("white")

        size = (200,100)

        armor_zone = DropZone(self._display_surface, (300,350), size)
        armor_zone.fill("green")

        weapon_zone = DropZone(self._display_surface, (300,550), size)
        weapon_zone.fill("blue")

        inventory_zone1 = DropZone(self._display_surface, (600,200), size, text= "Inventory1")
        inventory_zone1.fill("Grey")
        inventory_zone2 = DropZone(self._display_surface, (600,300), size, text= "Inventory2")
        inventory_zone2.fill("Grey")
        inventory_zone3 = DropZone(self._display_surface, (600,400), size, text= "Inventory3")
        inventory_zone3.fill("Grey")

        armor = Movable(self._display_surface, (0,0), size, "ARMOR :P")
        armor.fill("cyan")
        armor.set_zone(inventory_zone1)
        armor.register_zone(armor_zone)
        armor.register_zone(inventory_zone1)
        armor.register_zone(inventory_zone2)
        armor.register_zone(inventory_zone3)

        weapon = Movable(self._display_surface, (0,0), size, "SWORD D:")
        weapon.fill("magenta")
        weapon.set_zone(inventory_zone2)
        weapon.register_zone(weapon_zone)
        weapon.register_zone(inventory_zone1)
        weapon.register_zone(inventory_zone2)
        weapon.register_zone(inventory_zone3)

        weapon2 = Movable(self._display_surface, (0,0), size, "SWORD :O")
        weapon2.fill("magenta")
        weapon2.set_zone(inventory_zone3)
        weapon2.register_zone(weapon_zone)
        weapon2.register_zone(inventory_zone1)
        weapon2.register_zone(inventory_zone2)
        weapon2.register_zone(inventory_zone3)

        self.add_ui_element(armor_zone)
        self.add_ui_element(weapon_zone)
        self.add_ui_element(inventory_zone1)
        self.add_ui_element(inventory_zone2)
        self.add_ui_element(inventory_zone3)
        self.add_ui_element(armor)
        self.add_ui_element(weapon)
        self.add_ui_element(weapon2)


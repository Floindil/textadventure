from src.scenes.menu import Menu
from src.scenes.test_scene import TestScene
from src.resources.ui.elements import Button, UIElements
from src.resources.ui.controller import Controller
import pygame

class UI:

    _display_surface: pygame.Surface
    _elements: list[UIElements]

    def __init__(self, display_surface: pygame.Surface) -> None:
        self.controller = Controller()
        self._display_surface = display_surface

        self.menu = Menu(display_surface)
        self.last_scene = None
        self.scene = TestScene(self._display_surface)

        _last_scene_button = Button(display_surface, (300,300), (200,30), self.start_last_scene, "START")
        _last_scene_button.fill("white")
        self._menu_elements = [_last_scene_button]

        _menu_button = Button(display_surface, (10,10), (200, 30), self.start_menu, "MENU")
        _menu_button.fill("white")
        self._elements = [_menu_button]

        self.scene_elements = []


    def render(self):
        self.scene.render()
        for element in self.scene_elements:
            element.place()
        
    def start_menu(self):
        self.last_scene = self.scene
        self.scene = self.menu
        self.scene_elements = self._menu_elements + self.scene.buttons

    def start_last_scene(self):
        _last_scene = self.scene
        self.scene = self.last_scene
        self.last_scene = _last_scene
        self.scene_elements = self._elements + self.scene.buttons
        self.scene.add_controller(self.controller)

    def return_buttons(self):
        _list: list[Button] = []
        for element in self.scene_elements:
            if element.TAG == "Button":
                _list.append(element)
        return _list
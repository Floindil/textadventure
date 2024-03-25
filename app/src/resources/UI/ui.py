from src.scenes.menu import Menu
from src.scenes.scene import Scene
from src.scenes.test_scene import TestScene
from src.resources.ui.elements import Button, UIElement
from src.resources.ui.controller import Controller
import pygame

class UI:

    _display_surface: pygame.Surface
    scene_elements: list[UIElement]
    controller: Controller
    menu: Menu
    scene: Scene
    last_scene: Scene

    def __init__(self, display_surface: pygame.Surface) -> None:
        self.controller = Controller()
        self.run = True
        self._display_surface = display_surface

        self.menu = Menu(display_surface)
        self.last_scene = None
        self.scene = TestScene(self._display_surface)

        center = pygame.Vector2(self._display_surface.get_size())/2
        _button_size = pygame.Vector2(200,30)

        _quit_button = Button(self._display_surface, (self._display_surface.get_size()[0]-10-_button_size.x,10), _button_size, self.quit, "QUIT")
        _quit_button.fill("white")

        _last_scene_button = Button(self._display_surface, (center.x-_button_size.x/2,center.y-100), _button_size, self.start_last_scene, "RESUME")
        _last_scene_button.fill("white")
        self._menu_elements = [_last_scene_button, _quit_button]

        _menu_button = Button(self._display_surface, (10,10), _button_size, self.start_menu, "MENU")
        _menu_button.fill("white")
        self._elements = [_menu_button, _quit_button]

        self.scene_elements = []


    def render(self):
        self.scene.render()
        for element in self.scene_elements:
            element.render()

    def update(self, keys):
        self.controller.update_change(keys)
        current_position = self.scene.player.position
        temp_position = current_position + self.controller.raycast
        self.scene.player.update(temp_position)
        if self.scene.collisions:
            if not self.scene.check_bounds(self.scene.player) or self.scene.check_colliders(self.scene.player):
                self.scene.player.position.update(current_position)
            else: self.controller.update_position()
        
    def start_menu(self):
        self.last_scene = self.scene
        self.scene = self.menu
        self.scene_elements = self._menu_elements + self.scene.ui_elements

    def start_last_scene(self):
        _last_scene = self.scene
        self.scene: Scene = self.last_scene
        self.last_scene = _last_scene
        self.scene_elements = self._elements + self.scene.ui_elements
        self.scene.add_controller(self.controller)

    def return_elements(self) -> list[Button]:
        _list: list[UIElement] = []
        for element in self.scene_elements:
            if isinstance(element, UIElement):
                _list.append(element)
        return _list
    
    def quit(self):
        self.run = False
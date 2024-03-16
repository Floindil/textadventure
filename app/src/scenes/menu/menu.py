import pygame
from src.scenes.scene import Scene
from src.resources.ui.elements import Button

class Menu(Scene):
    def __init__(self, _display_surface: pygame.Surface) -> None:
        super().__init__(_display_surface)
        self.background.fill("grey")
        buttonsize = (300,50)
        displaySize = self.surface.get_size()
        buttonposition = (displaySize[0]/2-buttonsize[0]/2,displaySize[1]/2-buttonsize[1]/2)
        button = Button(self.surface,(buttonposition), buttonsize, self.some_action)
        button.fill("white")
        self.add_button(button)
    
    @staticmethod
    def some_action():
        print("action!")

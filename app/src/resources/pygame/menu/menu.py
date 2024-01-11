import pygame

class Menu:
    def __init__(self) -> None:
        pass

class Button:
    def __init__(self) -> None:
        button1images = [pygame.image.load("app/src/resources/pygame/button1up.png"),pygame.image.load("app/src/resources/pygame/button1down.png")]
        buttonsize = (195,71)
        buttonposition = (500,500)
        buttonstate = False
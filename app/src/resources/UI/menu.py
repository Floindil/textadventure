import pygame

class menu:
    def __init__(self, surface: pygame.surface) -> None:
        self.surface = surface
        

class Button:
    def __init__(self, coordinates: tuple, size: tuple, imagename: str, surface: pygame.surface, command):
        path = "app/src/resources/UI/"
        self.coordinates = coordinates
        self.command = command
        self.surface = surface
        self.size = size
        self.image = pygame.image.load(f"{path}{imagename}")
        self.rect = self.image.get_rect()

    def mousecheck(self):
        mousecoordinates = pygame.mouse.get_pos()
        check = self.rect.collidepoint(mousecoordinates[0], mousecoordinates[1])
        return check
    
    def place(self):
        self.surface.blit(self.image, self.coordinates)
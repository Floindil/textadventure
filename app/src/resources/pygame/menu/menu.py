import pygame

class Menu:
    def __init__(self) -> None:
        self.state = False
        self.button1 = Button("button1", (500,500))

    def update(self, surface: pygame.surface):
        surface.fill('green')
        self.button1.display(surface)

    def switch(self):
        if self.state:
            self.state = False
        else:
            self.state = True

class Button:
    def __init__(self, name: str, position:tuple) -> None:
        self.down = False
        path = "app/src/resources/pygame/menu/"
        self.images = [
            pygame.image.load(f"{path}{name}up.png"),
            pygame.image.load(f"{path}{name}down.png")
        ]
        self.position = position
        self.size = self.images[0].get_rect()
        self.size.move_ip(position[0],position[1])

    def display(self, surface: pygame.surface):
        surface.blit(self.images[int(self.down)], self.position)

    def point_check(self, point: tuple):
        return self.size.collidepoint(point[0],point[1])
    
    def press(self):
        point = pygame.mouse.get_pos()
        if self.size.collidepoint(point[0],point[1]):
            self.down = True

    def set_down(self, input: bool):
        self.down = input
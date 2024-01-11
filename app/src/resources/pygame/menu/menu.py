import pygame

class Menu:
    def __init__(self) -> None:
        self.state = False
        button1 = Button("button1", (500,500))
        button2 = Button("button1", (500,400))
        self.buttons = [button1, button2]

    def update(self, surface: pygame.surface):
        for button in self.buttons:
            button.display(surface)

    def switch(self):
        if self.state:
            self.state = False
        else:
            self.state = True
        
    def buttonactions(self):
        if self.buttons[0].down:
            print("close menu")
            self.state = False
            return True
        if self.buttons[1].down:
            print("quit Game")
            return False
        return True


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
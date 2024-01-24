import pygame

class Menu:
    def __init__(self) -> None:
        '''
        Class to hold the elements of the menu.
        '''
        self.state = False
        button1 = Button("button2", (500,500))
        button2 = Button("button1", (500,400))
        self.buttons = [button1, button2]

    def update(self, surface: pygame.surface):
        '''
        Displays the menu on the surface.
        Call from method to update the screen.
        '''
        surface.fill("blue")
        for button in self.buttons:
            button.display(surface)

    def set_state(self, state: bool):
        '''
        switches the "state" variable from True to False and vice versa.
        '''
        self.state = state
        
    def buttonactions(self):
        '''
        Methods for the buttons in the "buttons" list.
        '''
        if self.buttons[0].down:
            self.state = False
            return True
        if self.buttons[1].down:
            return False
        return True


class Button:
    def __init__(self, name: str, position:tuple) -> None:
        '''
        uses the name variable to load pngs for buttons in the menu folder.
        <<name>>up.png/<<name>>down.png
        position describes the top left corner of the button.
        '''
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
        '''
        displays the button on the surface.
        '''
        surface.blit(self.images[int(self.down)], self.position)
    
    def press(self):
        '''
        compares the mouse coordinates to the button and sets the "down" variable to True, if the point is inside the buttons rectangle.
        '''
        point = pygame.mouse.get_pos()
        if self.size.collidepoint(point[0],point[1]):
            self.down = True

    def set_down(self, input: bool):
        '''
        sets the "down" variable to the input value.
        '''
        self.down = input

    def switch(self):
        '''
        switches the "state" variable from True to False and vice versa.
        '''
        if self.down:
            self.down = False
        else:
            self.down = True
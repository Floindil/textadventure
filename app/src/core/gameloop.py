import pygame
from src.core.configuration import Configuration
from src.resources.ui.ui import UI
from src.scenes.menu import Menu

class Gameloop:

    display: pygame.display
    fps: int
    ui: UI
    clock: pygame.time.Clock
    menu: bool

    def __init__(self) -> None:
        displaySize = Configuration.DISPLAY_SIZE
        self.fps = Configuration.FPS
        self.display = pygame.display.set_mode(displaySize)
        pygame.display.set_caption("Textadventure")
        self.ui = UI(self.display)
        self.clock = pygame.time.Clock()
        self.ui.start_menu()
        self.menu = True

    def run(self):
        pygame.init()

        run = True

        while run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.menu:
                            self.ui.start_last_scene()
                            self.menu = False
                        else:
                            self.ui.start_menu()
                            self.menu = True
                        #pygame.mouse.set_visible(menu)
                        #pygame.mouse.set_pos(displaySize[0]/2,displaySize[1]/2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for element in self.ui.return_elements():
                        element.action()
                
                if event.type == pygame.MOUSEBUTTONUP:
                    for element in self.ui.return_elements():
                        if element.TAG == "Movable":
                            if element.grabbed:
                                element.drop()

            if isinstance(self.ui.scene, Menu):
                self.menu = True
            else: self.menu = False
            
            # define what happens outside of menu
            if not self.menu:
                keys = pygame.key.get_pressed()
                self.ui.update(keys)

            self.displayUpdate()

            run = self.ui.run

        pygame.quit()

    def displayUpdate(self):
        self.ui.render()
        pygame.display.update()
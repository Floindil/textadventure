import pygame
from src.core.configuration import Configuration
from src.scenes.menu.menu import Menu
from src.scenes.test_scene.test_scene import TestScene

class Gameloop:
    def __init__(self) -> None:
        displaySize = Configuration.DISPLAY_SIZE
        self.fps = Configuration.FPS
        self.display = pygame.display.set_mode(displaySize)
        pygame.display.set_caption("Textadventure")
        self.scene = Menu(self.display)
        self.clock = pygame.time.Clock()
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
                        self.change_scene()
                        #pygame.mouse.set_visible(menu)
                        #pygame.mouse.set_pos(displaySize[0]/2,displaySize[1]/2)
                if self.menu:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for b in self.scene.buttons:
                            if b.mousecheck():
                                b.action()
            
            # define what happens outside of menu
            if not self.menu:
                keys = pygame.key.get_pressed()

            self.displayUpdate()

        pygame.quit()

    def displayUpdate(self):
        self.scene.render()

        pygame.display.update()

    def change_scene(self):
            if isinstance(self.scene, Menu):
                self.scene = TestScene(self.display)
            else:
                self.scene = Menu(self.display)
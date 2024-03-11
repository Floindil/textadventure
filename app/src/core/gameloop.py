import pygame
from src.core.configuration import Configuration
from src.resources.UI.elements import Button

def gameloop():
    pygame.init()

    #region Setup
    displaySize = Configuration.DISPLAY_SIZE
    display = pygame.display.set_mode(displaySize)
    pygame.display.set_caption("Textadventure")

    clock = pygame.time.Clock()
    menu = True

    def some_action():
        print("action!")
    buttonsize = (300,50)
    buttonposition = (displaySize[0]/2-buttonsize[0]/2,displaySize[1]/2-buttonsize[1]/2)
    button = Button(display,(buttonposition), buttonsize,some_action)
    buttons = [button]


    #pygame.mouse.set_visible(menu)
    #endregion Setup

    def displayUpdate():
        if not menu:
            display.fill('blue')
        else:
            display.fill('grey')
            for b in buttons:
                b.place()

        pygame.display.update()

    run = True
    fps = 60

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if menu:
                        menu = False
                    else:
                        menu = True
                    #pygame.mouse.set_visible(menu)
                    #pygame.mouse.set_pos(displaySize[0]/2,displaySize[1]/2)
            if menu:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for b in buttons:
                        if b.mousecheck():
                            b.action()
        
        # define what happens outside of menu
        if not menu:
            keys = pygame.key.get_pressed()

        displayUpdate()

    pygame.quit()
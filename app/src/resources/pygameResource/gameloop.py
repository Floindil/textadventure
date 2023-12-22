import pygame

def gameloop():
    pygame.init()

    #region Setup
    displaySize = (1000,800)
    display = pygame.display.set_mode(displaySize)
    pygame.display.set_caption("Spirit Cards")

    clock = pygame.time.Clock()

    menu = False
    pygame.mouse.set_visible(menu)
    #endregion Setup

    def displayUpdate():
        if not menu:
            display.fill('white')
        else:
            display.fill('grey')
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
                    pygame.mouse.set_visible(menu)
                    pygame.mouse.set_pos(displaySize[0]/2,displaySize[1]/2)
        
        # define what happens outside of menu
        if not menu:
            keys = pygame.key.get_pressed()

        displayUpdate()

    pygame.quit()
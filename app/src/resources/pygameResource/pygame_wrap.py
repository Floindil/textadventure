import pygame
pygame.init()

display = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Spirit Cards")

clock = pygame.time.Clock()

menu = False
menu_cooldown = 0

def displayUpdate():
    if not menu:
        display.fill('blue')
    else:
        display.fill('green')
    pygame.display.update()

run = True

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if menu:
                    menu = False
                else:
                    menu = True

    keys = pygame.key.get_pressed()
    if menu > 0: menu_cooldown -= 1

    if keys[pygame.K_DELETE]:
            run = False

    if not menu_cooldown and event.type == pygame.KEYDOWN:
        menu_cooldown == 1
        if event.key == pygame.K_ESCAPE:
            if menu:
                menu = False
            else:
                menu = True

    if not menu:
        pass

    displayUpdate()
pygame.quit()

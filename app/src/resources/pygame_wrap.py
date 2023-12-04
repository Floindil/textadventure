# Example file showing a basic pygame "game loop"
import pygame
import os

'''# region pygame setup 1
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")
    tree = pygame.image.load('app/src/resources/tree.png')
    x = tree.get_width()/2
    y = tree.get_height()/2
    screen.blit(tree, (1280/2 - x, 720/2 - y))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
#endregion

'''
'''# region Example file showing a circle moving on screen

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
#endregion
'''

# region animation example
import pygame
pygame.init()

win = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("First Game")

def load_sprites(path):
    spriteImages = os.listdir(path)
    spriteLIst = []
    for sprite in spriteImages:
        image = pygame.image.load(f'{path}/{sprite}')
        spriteLIst.append(image)
    return spriteLIst


walkRight = load_sprites('app/src/resources/character1/walk_right')
walkLeft = load_sprites('app/src/resources/character1/walk_left')
attackRight = load_sprites('app/src/resources/character1/attack_right')
attackLeft = load_sprites('app/src/resources/character1/attack_left')
idleRight = load_sprites('app/src/resources/character1/idle_right')
idleLeft = load_sprites('app/src/resources/character1/idle_left')

bg = pygame.image.load('app/src/resources/bg.jpg')
char_right = pygame.image.load('app/src/resources/character1/walk_right/Walk1.png')
char_left = pygame.image.load('app/src/resources/character1/walk_left/Walk1.png')

x = 50
y = 400
width = 40
height = 60
vel = 10

clock = pygame.time.Clock()

isJump = False
isAttack = False
jumpCount = 10

left = False
right = False
walkCount = 0
idleCount = 0
attackCount = 0
direction = 'right'

def redrawGameWindow():
    global walkCount, idleCount, attackCount, vel, direction, isAttack, isJump, x
    
    win.blit(bg, bg.get_rect())  
    if walkCount + 1 >= 23:
        walkCount = 0
    
    if idleCount + 1 >= 23:
        idleCount = 0
        
    if isJump:
        walkCount = 0
        idleCount = 0
        if direction == 'right':
            win.blit(idleRight[0], (x,y))
        elif direction == 'left':
            win.blit(idleLeft[0], (x,y))
    elif isAttack:
        walkCount = 0
        idleCount = 0
        if direction == 'right':
            win.blit(attackRight[attackCount//3], (x,y))
            if 14 <= attackCount <= 17:
                x += 20
        elif direction == 'left':
            win.blit(attackLeft[attackCount//3], (x,y))
            if 14 <= attackCount <= 17:
                x -= 20
        attackCount += 1
        if attackCount == 24:
            attackCount = 0
            isAttack = False
            vel = 10
    elif left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
        direction = 'left'
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
        direction = 'right'
    elif direction == 'right':
        win.blit(idleRight[idleCount//6], (x, y))
        idleCount += 1
        walkCount = 0
    elif direction == 'left':
        win.blit(idleLeft[idleCount//6], (x, y))
        idleCount += 1
        walkCount = 0
        
    pygame.display.update() 
    


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_d] and x < 1920 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_w]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    if not(isAttack):
        if keys[pygame.K_e]:
            isAttack = True
            left = False
            right = False
            vel = 0

    redrawGameWindow() 
    
    
pygame.quit()
# endregion

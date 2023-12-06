# Example file showing a basic pygame "game loop"
import pygame
import os
from animation import Animator

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

bg = pygame.image.load('app/src/resources/bg.jpg')
char_right = pygame.image.load('app/src/resources/character1/idle/Idle1.png')
char_left = pygame.transform.flip(char_right, 1, 0)

x = 50
y = 400
width = 40
height = 60
vel = 10

walk = Animator('app/src/resources/character1/walk', win)
attack = Animator('app/src/resources/character1/attack', win)
idle = Animator('app/src/resources/character1/idle', win)

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
    global vel, direction, isAttack, isJump, x, walk, attack, idle
    
    win.blit(bg, bg.get_rect())
        
    if isJump:
        if direction == 'right':
            win.blit(char_right, (x,y))
        elif direction == 'left':
            win.blit(char_left, (x,y))
    elif isAttack:
        if direction == 'right':
            attack.run((x,y))
            if 14 <= attackCount <= 17:
                x += 20
        elif direction == 'left':
            attack.run((x,y), opposite_direction = True)
            if 14 <= attackCount <= 17:
                x -= 20
        if attack.count == attack.frames*3-1:
            isAttack = False
            vel = 10
    elif left:
        walk.run((x,y), opposite_direction = True)
        direction = 'left'
    elif right:
        walk.run((x,y))
        direction = 'right'
    elif direction == 'right':
        idle.run((x,y), animation_speed = 2)
    elif direction == 'left':
        idle.run((x,y), animation_speed = 2, opposite_direction = True)
        
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

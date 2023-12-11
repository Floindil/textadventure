# Example file showing a basic pygame "game loop"
import pygame
from animation import Animator
from bglayout import level_bg

# region animation example
import pygame
pygame.init()

win = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Spirit Cards")

bg = pygame.image.load('app/src/resources/bg.jpg')
char_right = pygame.image.load('app/src/resources/character1/idle/Idle1.png')
char_right = pygame.transform.scale(char_right, (char_right.get_rect().bottomright[0]/2, char_right.get_rect().bottomright[1]/2))
char_left = pygame.transform.flip(char_right, 1, 0)

x = 250
y = level_bg.calc_y(x)
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
falling = False
walkCount = 0
idleCount = 0
attackCount = 0
fallCount = 0
direction = 'right'
menu = False
menu_cooldown = 0

def redrawGameWindow():
    global vel, direction, isAttack, isJump, x, walk, attack, idle, menu, y, falling
    
    win.blit(bg, bg.get_rect())
    
    if menu:
        win.fill('green')
    elif isJump:
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

    if not menu_cooldown and event.type == pygame.KEYDOWN:
        menu_cooldown == 1
        if event.key == pygame.K_ESCAPE:
            if menu:
                menu = False
            else:
                menu = True

    if not menu:
        if keys[pygame.K_DELETE]:
            run = False
        
        if keys[pygame.K_a] and x > vel:
            if not level_bg.wall_check(x - vel, y):
                x -= vel
            y = level_bg.calc_y(x)
            left = True
            right = False

        elif keys[pygame.K_d] and x < 1920 - vel - width:
            if not level_bg.wall_check(x + vel, y):
                x += vel
            y = level_bg.calc_y(x)
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
            gc = level_bg.ground_check(x)
            if jumpCount >= -10:
                y -= int((jumpCount * abs(jumpCount)) * 0.5)
                if y >= gc:
                    jumpCount = 10
                    isJump = False
                else:
                    jumpCount -= 1
            else:
                y = gc
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

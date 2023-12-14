# Example file showing a basic pygame "game loop"
import pygame
from animation import Animator
from moveset import Moveset
from bglayout import level_bg

# region animation example
import pygame
pygame.init()

win = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Spirit Cards")

bg = pygame.image.load('app/src/resources/bg.jpg')
char_right = pygame.image.load('app/src/resources/character1/idle/Idle-1.png')
char_right = pygame.transform.scale(char_right, (char_right.get_rect().bottomright[0]/2, char_right.get_rect().bottomright[1]/2))
char_left = pygame.transform.flip(char_right, 1, 0)

x = 250
y = level_bg.calc_y(x)
width = 40
height = 60
vel = 10

player_moveset = Moveset(
    screen = win,
    animationPath = 'app/src/resources/character1/',
    animations = [
        'idle',
        'walk',
        'attack',
        'jump',
        'roll'
    ]
)

attack_effect = Animator('app/src/resources/effects/attack', win)

creature_x = 1000
creature_y = level_bg.calc_y(creature_x)
creature1_moveset = Moveset(win, 'app/src/resources/creature1/')

clock = pygame.time.Clock()

menu = False
menu_cooldown = 0

def redrawGameWindow():
    global vel, direction, isAttack, isJump, x, walk, attack, idle, menu, y, falling
    
    win.blit(bg, bg.get_rect())
    
    if menu:
        win.fill('green')
    else:

        creature1_moveset.run(creature_x, creature_y)
        player_moveset.run(x, y)
        if player_moveset.state == 'attack':
            if player_moveset.direction == 'right':
                attack_effect.run((x+160,y))
            elif player_moveset.direction == 'left':
                attack_effect.run((x-160,y), opposite_direction = True)
        
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

    #region Player behaviour
        if player_moveset.state == 'walk':
            player_moveset.set_state('idle')
        
        if player_moveset.state == 'idle':
            if keys[pygame.K_a] and x > vel:
                player_moveset.direction = 'left'
                player_moveset.set_state('walk')
                if not level_bg.wall_check(x-vel, y):
                    x -= vel
                if player_moveset.state != 'jump':
                    y = level_bg.calc_y(x)

            elif keys[pygame.K_d] and x < 1920 - vel - width:
                player_moveset.direction = 'right'
                player_moveset.set_state('walk')
                if not level_bg.wall_check(x+vel, y):
                    x += vel
                if player_moveset.state != 'jump':
                    y = level_bg.calc_y(x)
        
        if player_moveset.state == 'idle' or player_moveset.state == 'walk':
            if keys[pygame.K_e]:
                player_moveset.set_state('attack')
                vel = 0
            elif keys[pygame.K_SPACE]:
                last_y = y
                if player_moveset.state == 'walk':
                    previous_state = 'walk'
                elif player_moveset.state == 'idle':
                    previous_state = 'idle'
                player_moveset.set_state('jump')
            elif keys[pygame.K_LSHIFT]:
                player_moveset.set_state('roll')
        
        if player_moveset.state == 'attack':
            if player_moveset.animations.get('attack').cycles >= 1 and not keys[pygame.K_e]:
                player_moveset.animations.get('attack').reset()
                player_moveset.set_state('idle')
                vel = 10

        if player_moveset.state == 'jump':
            if previous_state == 'walk':
                if player_moveset.direction == 'right':
                    if not level_bg.wall_check(x+vel, y):
                        x += vel
                elif player_moveset.direction == 'left':
                    if not level_bg.wall_check(x-vel, y):
                        x -= vel
            frames = player_moveset.animations.get('jump').frames*3-1
            count = player_moveset.animations.get('jump').count
            add_y = int(((count-frames/2)**2 - (frames/2)**2)*4)
            y = last_y + add_y
            if count >= frames/2 and y >= level_bg.ground_check(x) or player_moveset.animations.get('jump').cycles >= 1 and not keys[pygame.K_SPACE]:
                y = level_bg.calc_y(x)
                player_moveset.animations.get('jump').reset()
                player_moveset.set_state('idle')

        if player_moveset.state == 'roll':
            if player_moveset.direction == 'right':
                if not level_bg.wall_check(x+vel, y):
                    if not level_bg.wall_check(x+vel*2, y):
                        x += vel*2
            elif player_moveset.direction == 'left':
                if not level_bg.wall_check(x-vel, y):
                    if not level_bg.wall_check(x-vel*2, y):
                        x -= vel*2
            y = level_bg.calc_y(x)
            if player_moveset.animations.get('roll').cycles >= 1 and not keys[pygame.K_e]:
                player_moveset.animations.get('roll').reset()
                player_moveset.set_state('idle')

        #endregion

    #region Creature behaviour

        creature1_moveset.state = 'walk'

        if creature_x >= 1500: creature1_moveset.direction = 'left'
        elif creature_x <= 1000: creature1_moveset.direction = 'right'

        if creature1_moveset.direction == 'left': creature_x -= 10
        elif creature1_moveset.direction == 'right': creature_x += 10

        #endregion

    redrawGameWindow()
    
    
pygame.quit()
# endregion

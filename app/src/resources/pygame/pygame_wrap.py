# Example file showing a basic pygame "game loop"
import pygame
from animation import Animator
from moveset import Moveset
from bglayout import level_bg
from menu.menu import Menu

# region animation example
pygame.init()

win = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
pygame.display.set_caption("Spirit Cards")

bg = pygame.image.load('app/src/resources/bg.jpg')

x = 250
y = level_bg.calc_y(x)
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
creature_y = level_bg.calc_y(creature_x) + 100
creature_vel = 7
creature1_moveset = Moveset(win, 'app/src/resources/creature1/')

clock = pygame.time.Clock()

menu = Menu()

def redrawGameWindow():
    global vel, x, y
    
    win.blit(bg, bg.get_rect())
    
    if menu.state:
        menu.update(win)
        
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
creature_cooldown = 0

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if menu.state:
                    menu.switch()
                else:
                    menu.switch()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DELETE]:
            run = False
    if menu.state:
        if pygame.mouse.get_pressed()[0]:
            for button in menu.buttons:
                button.press()
        else:
            for button in menu.buttons:
                button.set_down(False)
        run = menu.buttonactions()

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

            elif keys[pygame.K_d] and x < 1920 - vel:
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
            if count >= frames/2 and y >= level_bg.ground_check(x) or player_moveset.animations.get('jump').cycles >= 1:
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
        if creature1_moveset.state != 'attack':
            if creature1_moveset.direction == 'right' and creature_x >= 1500 or creature1_moveset.direction == 'left' and creature_x <= 1000:
                creature1_moveset.set_state('idle')
            if abs(creature_x - x) < 150 and creature_cooldown == 0:
                if creature_x - x < 0:creature1_moveset.set_direction('right')
                else: creature1_moveset.set_direction('left')
                creature1_moveset.set_state('attack')
        
        if creature1_moveset.animations.get('idle').cycles >= 5:
            creature1_moveset.animations.get('idle').reset()
            if creature1_moveset.direction == 'right':
                creature1_moveset.set_direction('left')
            elif creature1_moveset.direction == 'left':
                creature1_moveset.set_direction('right')
            creature1_moveset.set_state('walk')

        if creature1_moveset.state == 'walk':
            if creature1_moveset.direction == 'left': creature_x -= creature_vel
            elif creature1_moveset.direction == 'right': creature_x += creature_vel

        if creature_cooldown > 0: creature_cooldown -= 1

        if creature1_moveset.state == 'attack':
            ca = creature1_moveset.animations.get('attack')
            if creature1_moveset.direction == 'right':
                if ca.count == 18:
                    creature_x += 150
                if ca.count in (19, 20): 
                    creature_x += 5
            elif creature1_moveset.direction == 'left':
                if ca.count == 18:
                    creature_x -= 150
                if ca.count in (19, 20): 
                    creature_x -= 5
            if ca.cycles >= 1:
                creature_cooldown = 10
                creature1_moveset.set_state('walk')
                creature1_moveset.animations.get('attack').reset()

        #endregion

    redrawGameWindow()
    
pygame.quit()
# endregion

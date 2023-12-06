import os
import pygame

class Animator:
    '''
    Handles Animations, uses sprite_path to load the animationsprites
    Animationsprites must be named and ordered chronologically
    display: Where the Animation will be played
    if state = False: Animation will be blocked
    '''
    def __init__(self, sprite_path: str, display: pygame.display) -> None:
        self.dispaly = display
        self.spritelist = self.sprite_loader(sprite_path = sprite_path)
        self.frames = len(self.spritelist)
        self.count = 0
        self.state = True

    def run(self, position: tuple, animation_speed: int = 1, opposite_direction: bool = False):
        '''
        Displays the Animationframe depending on the Animations count
        '''
        speed = animation_speed * 3
        if self.state:
            image = self.spritelist[self.count//speed]
            if opposite_direction:
                image = pygame.transform.flip(image, 1, 0)
            self.dispaly.blit(image, position)
            self.count +=1
            if self.count > self.frames * 3 - 1:
                self.count = 0

    @staticmethod
    def sprite_loader(sprite_path):
        '''
        loads sprites from path and returns list of pygame.image objects.
        '''
        spriteImages = os.listdir(sprite_path)
        spriteLIst = []
        for sprite in spriteImages:
            image = pygame.image.load(f'{sprite_path}/{sprite}')
            spriteLIst.append(image)
        return spriteLIst
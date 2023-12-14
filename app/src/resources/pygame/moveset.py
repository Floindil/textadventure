from animation import Animator

class Moveset:
    def __init__(self, screen, animationPath: str, animations: list = ['idle', 'walk', 'attack']) -> None:
        self.animationPath = animationPath
        self.direction = 'right'
        self.state = 'idle'
        self.animations = {}
        for animation in animations:
            a = Animator(f'{animationPath}{animation}', screen)
            self.animations.update({animation: a})

    def run(self, x: int, y: int):
        animation = self.animations.get(self.state)
        if self.direction == 'right':
            animation.run((x,y))
        elif self.direction == 'left':
            animation.run((x,y), opposite_direction = True)

    def set_state(self, state: str):
        self.state = state

    def set_direction(self, direction: str):
        self.direction = direction
import pygame

class Controller:
    position : pygame.Vector3

    def __init__(self) -> None:
        self.speed = 10
        self.position = pygame.Vector3(200,200,0)
        self.configuration = {
            "up": {
                "key": pygame.K_w,
                "action": self.up_action
            },
            "down": {
                "key": pygame.K_s,
                "action": self.down_action
            },
            "right": {
                "key": pygame.K_d,
                "action": self.right_action
            },
            "left": {
                "key": pygame.K_a,
                "action": self.left_action
            }
        }

    def update(self, keys):
        for key in self.configuration:
            k = self.configuration.get(key)
            if keys[k.get("key")]:
                action = k.get("action")
                action()

    def up_action(self):
        self.position.y -= 1 * self.speed
    def down_action(self):
        self.position.y += 1 * self.speed
    def right_action(self):
        self.position.x += 1 * self.speed
    def left_action(self):
        self.position.x -= 1 * self.speed

    def get_position(self):
        return self.position
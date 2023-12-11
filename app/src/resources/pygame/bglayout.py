platforms = [
    [0, 270, 680, 680],
    [270, 440, 680, 590],
    [440, 460, 590, 590],
    [460, 550, 800, 800],
    [550, 2000, 495, 495]
]
walls = [
    [460, 800, 590],
    [550, 800, 495]
]

class Levelhandler:
    def __init__(self, platforms: list, walls: list) -> None:
        self.platforms = platforms
        self.walls = walls

    def calc_y(self, x):
        '''
        uses an Array of lists with entries like: [start x, end x, start y, end y]
        to calculate y points in between start and end x
        '''
        for platform in self.platforms:
            if x < platform[1]:
                if platform[2] == platform[3]:
                    y = platform[2]
                else:
                    diff_x = platform[1] - platform[0]
                    diff_y = platform[2] - platform[3]
                    part_y = diff_y/diff_x*(x - platform[0])
                    y = platform[2] - part_y
                return y
    
    def ground_check(self, x: int):
        for platform in self.platforms:
            if x < platform[1]:
                return self.calc_y(x)
            
    def wall_check(self, x: int, y: int):
        for wall in self.walls:
            if x == wall[0] and wall[1] > y > wall[2]:
                return True
            else: return False
            
level_bg = Levelhandler(platforms, walls)
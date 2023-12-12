platforms = [
    [0, 270, 660, 660],
    [270, 440, 660, 570],
    [440, 460, 570, 570],
    [460, 550, 700, 700],
    [550, 2000, 475, 475]
]
walls = [
    [460, 801, 570],
    [550, 801, 475]
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
            if x == wall[0] and y < wall[1] and y > wall[2]:
                return True
        return False
            
level_bg = Levelhandler(platforms, walls)
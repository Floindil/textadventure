platform_heights = [
    [0, 270, 680, 680],
    [270, 440, 680, 590],
    [440, 550, 800, 800],
    [550, 2000, 495, 495]
]

class Levelhandler:
    def __init__(self, platform_heights: list) -> None:
        self.ph = platform_heights

    def calc_y(self, x):
        '''
        uses an Array of lists with entries like: [start x, end x, start y, end y]
        to calculate y points in between start and end x
        '''
        for part in self.ph:
            if x < part[1]:
                if part[2] == part[3]:
                    y = part[2]
                else:
                    diff_x = part[1] - part[0]
                    diff_y = part[2] - part[3]
                    part_y = diff_y/diff_x*(x - part[0])
                    y = part[2] - part_y
                return y
    
    def ground_check(self, x):
        for part in self.ph:
            if x < part[1]:
                return self.calc_y(x)
            
level_bg = Levelhandler(platform_heights)
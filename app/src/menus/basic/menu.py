from ...resources.tkresource import Window
from ...assets.player import player

class Menu:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.master = None

    def open(self, master):
        self.window = Window(self.title, self.width, self.height, master)
        self.master = self.window.window
        self.master.focus_force()

    def close(self):
        self.window.window.destroy()
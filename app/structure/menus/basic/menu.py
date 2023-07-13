from ...resources.tkresource import Window, Widgets
from ...resources.configuration.settings import playercreationconfig

class Menu:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.master = None

    def open(self, master):
        self.window = Window(master, self.title, self.width, self.height)
        self.master = self.window.window
        self.master.focus_force()

    def close(self):
        self.window.window.destroy()
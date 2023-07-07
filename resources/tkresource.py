from tkinter import Tk, Button, Label, Listbox, Toplevel
from .configuration.settings import rootsize

root = Tk()
root.title('Adventure')
root_width = int(rootsize['width'])
root_height = int(rootsize['height'])
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - root_width/2)
center_y = int(screen_height/2 - root_height/2)
root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
root.update_idletasks()

class Widgets:
    def __init__(self, master, x : int, y : int, anchor : str):
        self.master = master
        self.x = x
        self.y = y
        self.anchor = anchor

    def label(self, text : str):
        self.widget = Label(self.master, text = text)
        self.widget.place(x = self.x, y = self.y, anchor = self.anchor)

    def button(self, text : str, command):
        self.widget = Button(self.master, text = text, command = command)
        self.widget.place(x = self.x, y = self.y, anchor = self.anchor)

    def listbox(self, width : int, height : int, content : list):
        self.widget = Listbox(self.master, width = width, height = height, justify = 'center')
        self.widget.place(x = self.x, y = self.y, anchor = self.anchor)
        for item in content:
            self.widget.insert('end', item)

class Window:
    def __init__(self, master, title : str, width : int, height : int):
        self.window = Toplevel(master)
        self.window.title = title
        master_width = master.winfo_width()
        master_height = master.winfo_height()
        master_x = master.winfo_x()
        master_y = master.winfo_y()
        position_x = int(master_x) - width/2 + int(master_width/2)
        position_y = int(master_y) - height/2 + int(master_height/2)
        self.window.geometry(f'{width}x{height}+{int(position_x)}+{int(position_y)}')

    def set_fullscreen(self):
        self.window.attributes('-fullscreen', True)
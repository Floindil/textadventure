from tkinter import Tk, Button, Label, Listbox, Entry, Toplevel
from .configuration.settings import rootconfig, padding

root = Tk()
root.title(rootconfig['GameName'])
root_width = int(rootconfig['RootWidth'])
root_height = int(rootconfig['RootHeight'])
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - root_width/2)
center_y = int(screen_height/2 - root_height/2)
root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
value = int(padding['BorderPadding'])
rootpadding = {
    'pad_left' : value,
    'pad_right' : screen_width - value,
    'pad_top' : value,
    'pad_bottom' : root_height - value
}
        
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

    def entry(self, width : int):
        self.widget = Entry(self.master, width = width)
        self.widget.place(x = self.x, y = self.y, anchor = self.anchor)

class Window:
    def __init__(self, master, title : str, width : int, height : int):
        self.window = Toplevel(master)
        self.window.title = title
        master_width = master.winfo_width()
        master_height = master.winfo_height()
        master_x = master.winfo_x()
        master_y = master.winfo_y()
        center_x = int(master_x) - width/2 + int(master_width/2)
        center_y = int(master_y) - height/2 + int(master_height/2)
        self.window.geometry(f'{width}x{height}+{int(center_x)}+{int(center_y)}')
        self.center_x = width / 2
        self.center_y = height / 2
        self.pad_left = value
        self.pad_right = width - value
        self.pad_top = value
        self.pad_bottom = height - value
        self.pad_line = padding['LinePadding']

    def enable_fullscreen(self):
        self.window.attributes('-fullscreen', True)

    def disable_fullscreen(self):
        self.window.attributes('-fullscreen', False)
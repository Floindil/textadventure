from tkinter import Tk, Button, Label, Listbox, Entry, Toplevel, Scrollbar, Frame
from .configuration.settings import rootconfig

root = Tk()
root.title(rootconfig['Name'])
root_width = int(rootconfig['Width'])
root_height = int(rootconfig['Height'])
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - root_width/2)
center_y = int(screen_height/2 - root_height/2)
root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')        
root.update_idletasks()

class Widgets:
    def __init__(self, master, column : int, row : int):
        self.master = master
        self.column = column
        self.row = row
        self.pad = 10

    def label(self, text : str):
        self.widget = Label(self.master, text = text)
        self.widget.grid(column = self.column, row = self.row, padx = self.pad, pady = self.pad)

    def button(self, text : str, command):
        self.widget = Button(self.master, text = text, command = command)
        self.widget.grid(column = self.column, row = self.row, padx = self.pad, pady = self.pad)

    def listbox(self, width : int, height : int, content : list):
        self.widget = Listbox(self.master, width = width, height = height, justify = 'center')
        self.widget.pack(side = 'left', fill = 'y')
        for item in content:
            self.widget.insert('end', item)

    def scrollbar(self, to_scroll):
        self.widget = Scrollbar(self.master)
        self.widget.pack(side = 'right', fill = 'y')
        to_scroll.config(yscrollcommand = self.widget.set)
        self.widget.config(command = to_scroll.yview)

    def entry(self, width : int):
        self.widget = Entry(self.master, width = width)
        self.widget.grid(column = self.column, row = self.row, padx = self.pad, pady = self.pad)
    
    def frame(self):
        self.widget = Frame(self.master)
        self.widget.grid(column = self.column, row = self.row, padx = self.pad, pady = self.pad)

    def change_lb_content(self, new_content: list):
        self.widget.delete(0, 'end')
        for item in new_content:
            self.widget.insert('end', item)

class Window:
    def __init__(self, master, title : str, width : int, height : int):
        self.window = Toplevel(master)
        self.window.title = title
        self.window.grid_anchor('center')
        master_width = master.winfo_width()
        master_height = master.winfo_height()
        master_x = master.winfo_x()
        master_y = master.winfo_y()
        center_x = int(master_x) - width/2 + int(master_width/2)
        center_y = int(master_y) - height/2 + int(master_height/2)
        self.window.geometry(f'{width}x{height}+{int(center_x)}+{int(center_y)}')
        self.center_x = width / 2
        self.center_y = height / 2

    def enable_fullscreen(self):
        self.window.attributes('-fullscreen', True)

    def disable_fullscreen(self):
        self.window.attributes('-fullscreen', False)
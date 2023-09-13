from .basic.menu import Menu
from ..resources.tkresource import root, Widgets, Window
from ..resources.configuration.settings import rootconfig, loadwinconfig
from ..assets.data.datahandler import datahandler, datapath
from ..assets.player import player
from .playercreation import PlayerCreation
import os
from .inventory import inventory

class Mainmenu(Menu):
    def __init__(self):
        self.width = rootconfig.get('Width')
        self.height = rootconfig.get('Height')
        root.grid_anchor('center')
        self.load_newest()

    def open(self):

        ### Left Frame ###

        left_frame = Widgets(root, 0, 0)
        left_frame.frame()
        left_frame.widget.configure(width = self.width/2)

        new_game = Widgets(left_frame.widget, 0, 1)
        new_game.button('New Game', self.new)
        new_game.widget.configure(width = 10)

        self.cont = Widgets(left_frame.widget, 0, 2)
        self.cont.button('Continue', self.load_newest)
        self.cont.widget.configure(width = 10)

        self.loading = Widgets(left_frame.widget, 0, 3)
        self.loading.button('Load Game', self.load_win)
        if os.listdir(datapath) == []:
            self.loading.widget.configure(state = 'disabled')
            self.cont.widget.configure(state = 'disabled')
        self.loading.widget.configure(width = 10)

        self.cont = Widgets(left_frame.widget, 0, 4)
        self.cont.button('Inventory', lambda: inventory.open(root))
        self.cont.widget.configure(width = 10)

        ### Left Frame ###

        ### Right Frame ###

        right_frame = Widgets(root, 1, 0)
        right_frame.frame()
        right_frame.widget.configure(width = self.width/2)

        infotext = self.create_text()
        self.info = Widgets(right_frame.widget,  0, 0)
        self.info.label(infotext)
        self.info.widget.configure(justify = 'left')
        if os.listdir(datapath) == []:
            self.info.widget.configure(state = 'disabled')

        valuetext = self.create_text(1)
        self.valuelabel = Widgets(right_frame.widget,  1, 0)
        self.valuelabel.label(valuetext)
        self.valuelabel.widget.configure(justify = 'right')

        ### Right Frame ###

    def new(self):
        pc = PlayerCreation()
        pc.open(master= root)

    def load_newest(self):
        savefiles = datahandler.list_savefiles()
        if savefiles != []:
            savefiles.sort(key=lambda x: os.path.getmtime(f'{datapath}{x}.json'), reverse = True)
            name = savefiles[0]
            datahandler.load(name)
        self.update

    def update(self):
        if os.listdir(datapath) == []:
            self.loading.widget.configure(state = 'disabled')
            self.cont.widget.configure(state = 'disabled')
            self.info.widget.configure(state = 'disabled')
            valuetext = ''
        else:
            self.loading.widget.configure(state = 'active')
            self.cont.widget.configure(state = 'active')
            self.info.widget.configure(state = 'active')
            valuetext = self.create_text(1)
        self.valuelabel.widget.configure(text = valuetext)

    def load_win(self):
        width = loadwinconfig.get('Width')
        height = loadwinconfig.get('Height')
        self.win = Window('Select File', width, height)
        winmaster = self.win.window
        winmaster.focus_force()

        Widgets(winmaster, 1, 1).label('Select Savefile')

        ### Listbox Frame ###

        self.f = Widgets(winmaster, 1, 2)
        self.f.frame()

        lb_height = loadwinconfig.get('LB_Height')
        lb_width = loadwinconfig.get('LB_Width')
        savefiles = datahandler.list_savefiles()
        savefiles.sort(key=lambda x: os.path.getmtime(f'{datapath}{x}.json'), reverse = True)
        self.lb = Widgets(self.f.widget, None, None)
        self.lb.listbox(lb_width, lb_height, savefiles)
        
        if lb_height < len(savefiles):
            scrollbar = Widgets(self.f.widget, None, None)
            scrollbar.scrollbar(self.lb.widget)

        ### Listbox Frame ###

        self.label = Widgets(winmaster, 1, 6)
        self.label.label('')

        load = Widgets(winmaster, 1, 3)
        load.button('Load', command = lambda: self.load(self.lb.widget))
        load.widget.configure(width = '7')

        cancel = Widgets(winmaster, 0, 6)
        cancel.button('Cancel', self.cancel)
        cancel.widget.configure(width = '7')

        delete = Widgets(winmaster, 2, 6)
        delete.button('Delete', lambda: self.delete(self.lb.widget))
        delete.widget.configure(width = '7')

    def cancel(self):
        self.win.window.destroy()
        self.update()

    def delete(self, listbox):
        listbox = listbox
        index = listbox.curselection()
        if index == ():
            self.label.widget.configure(text = 'please select a file')
        else:
            name = listbox.get(index)
            os.remove(f'{datapath}{name}.json')
            self.lb.widget.delete(index)
            self.load_newest()

    def load(self, listbox):
        listbox = listbox
        index = listbox.curselection()
        if index == ():
            self.label.widget.configure(text = 'please select a file')
        else:
            name = listbox.get(index)
            datahandler.load(name)
            self.update()
            self.win.window.destroy()

    def create_text(self, value: int = 0):
        text = f'{player.list_dict(player.info, value)}\n\n{player.list_dict(player.attributes, value)}'
        return text
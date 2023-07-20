from ..resources.tkresource import root, Widgets, Window
from ..resources.configuration.settings import rootconfig, loadwinconfig, padding
from ..assets.data.datahandler import datahandler, datapath
from ..assets.player import player
from .playercreation import PlayerCreation
import os

class Mainmenu:
    def __init__(self):
        self.width = rootconfig['Width']
        self.height = rootconfig['Height']
        self.load_newest()

    def open(self):
        pad = padding['BorderPadding']
        pad2 = padding['LinePadding2']
        center = self.width/2

        ng = Widgets(root, center/2, self.height/2, 'center')
        ng.button('New Game', self.new)
        ng.widget.configure(width = 10)

        self.cont = Widgets(root, center/2, self.height/2 - pad2, 'center')
        self.cont.button('Continue', self.load_newest)
        self.cont.widget.configure(width = 10)

        self.loading = Widgets(root, center/2, self.height/2 + pad2, 'center')
        self.loading.button('Load Game', self.load_win)
        if os.listdir(datapath) == []:
            self.loading.widget.configure(state = 'disabled')
            self.cont.widget.configure(state = 'disabled')
        self.loading.widget.configure(width = 10)

        infotext = self.create_text()
        self.info = Widgets(root, center, self.height/2, 'w')
        self.info.label(infotext)
        self.info.widget.configure(justify = 'left')
        if os.listdir(datapath) == []:
            self.info.widget.configure(state = 'disabled')

        valuetext = self.create_text(1)
        self.valuelabel = Widgets(root, center+center/2, self.height/2, 'w')
        self.valuelabel.label(valuetext)
        self.valuelabel.widget.configure(justify = 'left')

    def new(self):
        pc = PlayerCreation()
        pc.open(master= root)

    def create_text(self, value: int = 0):
        text = f'{player.list_dict(player.info, value)}\n\n{player.list_dict(player.attributes, value)}'
        return text

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
        else:
            self.loading.widget.configure(state = 'active')
            self.cont.widget.configure(state = 'active')
            self.info.widget.configure(state = 'active')
        valuetext = self.create_text(1)
        self.valuelabel.widget.configure(text = valuetext)

    def load_win(self):
        width = loadwinconfig['Width']
        height = loadwinconfig['Height']
        self.win = Window(root, 'Select File', width, height)
        winmaster = self.win.window
        winmaster.focus_force()

        Widgets(winmaster, width/2, self.win.pad, 'n').label('Select Savefile')

        self.f = Widgets(winmaster, width/2, self.win.pad_line2, 'n')
        self.f.frame()

        lb_height = loadwinconfig['LB_Height']
        lb_width = loadwinconfig['LB_Width']
        savefiles = datahandler.list_savefiles()
        savefiles.sort(key=lambda x: os.path.getmtime(f'{datapath}{x}.json'), reverse = True)
        self.lb = Widgets(self.f.widget, None, None, None)
        self.lb.listbox(lb_width, lb_height, savefiles)
        
        if lb_height < len(savefiles):
            scrollbar = Widgets(self.f.widget, None, None, None)
            scrollbar.scrollbar(self.lb.widget)

        self.label = Widgets(winmaster, width/2, self.win.pad_opposite - self.win.pad_line2, 's')
        self.label.label('')

        load = Widgets(winmaster, width - self.win.pad, self.win.pad_opposite, 'se')
        load.button('Load', command = lambda: self.load(self.lb.widget))
        load.widget.configure(width = '7')

        cancel = Widgets(winmaster, self.win.pad, self.win.pad_opposite, 'sw')
        cancel.button('Cancel', self.cancel)
        cancel.widget.configure(width = '7')

        delete = Widgets(winmaster, width/2, self.win.pad_opposite, 's')
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
from ..resources.tkresource import root, Widgets, Window
from ..resources.configuration.settings import rootconfig, loadwinconfig, padding
from ..assets.data.datahandler import datahandler
from .playercreation import PlayerCreation

class Mainmenu:
    def __init__(self):
        self.width = rootconfig['Width']
        self.height = rootconfig['Height']

    def open(self):
        pad = padding['BorderPadding']
        pad2 = padding['LinePadding2']
        center = self.width/2
        Widgets(root, center, pad2, 'n').button('New Game', self.new)
        self.loading = Widgets(root, center, pad + 2* pad2, 'n')
        self.loading.button('Load Game', self.load_win)

    def new(self):
        pc = PlayerCreation()
        pc.open(master= root)

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
        self.lb = Widgets(self.f.widget, None, None, None)
        self.lb.listbox(lb_width,lb_height,savefiles)
        
        if lb_height < len(savefiles):
            scrollbar = Widgets(self.f.widget, None, None, None)
            scrollbar.scrollbar(self.lb.widget)

        self.label = Widgets(winmaster, width/2, self.win.pad_opposite, 's')
        self.label.label('')

        load = Widgets(winmaster, width - self.win.pad, self.win.pad_opposite, 'se')
        load.button('Load', command = lambda: self.load(self.lb.widget))
        cancel = Widgets(winmaster, self.win.pad, self.win.pad_opposite, 'sw')
        cancel.button('Cancel', winmaster.destroy)

    def load(self, listbox):
        listbox = listbox
        index = listbox.curselection()
        if index == ():
            self.label.widget.configure(text = 'please select a file')
        else:
            name = listbox.get(index)
            datahandler.load(name)
            self.win.window.destroy()
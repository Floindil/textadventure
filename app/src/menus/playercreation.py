from .basic.menu import *
from ..assets.player import player
from ..assets.data.datahandler import datahandler
from ..resources.configuration.settings import playercreationconfig
from ..resources.tkresource import Widgets

class PlayerCreation(Menu):
    def __init__(self):
        width = playercreationconfig['Width']
        height = playercreationconfig['Height']
        super().__init__(title = 'Character Creation', width = width, height = height)
        self.data = {
            'Race' : None,
            'Sex' : None
        }

    def open(self, master):
        super().open(master)

        ### Name Frame ###

        name_frame = Widgets(self.master, 1, 0)
        name_frame.frame()
        name_frame.widget.grid_anchor('w')
        name_frame.widget.grid(sticky = 'W')

        namelabel = Widgets(name_frame.widget, 0, 0)
        namelabel.label('Choose your Name:')
        namelabel.widget.grid(sticky = 'W')

        self.nameselect = Widgets(name_frame.widget, 1, 0)
        self.nameselect.entry(20)
        self.nameselect.widget.grid(sticky = 'W')

        ### Name Frame ###

        ### Frame ###

        frame = Widgets(self.master, 1, 1)
        frame.frame()
        frame.widget.grid_anchor('w')

        sex = []
        sexlabel = Widgets(frame.widget, 0, 1)
        sexlabel.label('Choose your Sex:')
        sexlabel.widget.grid(sticky = 'W')

        SelectButton(frame.widget, 1, 1, 'Female', 'Sex', sex, self.data)
        SelectButton(frame.widget, 2, 1, 'Male', 'Sex', sex, self.data)

        racelabel = Widgets(frame.widget, 0, 2)
        racelabel.label('Choose your Race:')
        racelabel.widget.grid(sticky = 'W')

        races = []
        SelectButton(frame.widget, 1, 2, 'Human', 'Race', races, self.data)
        SelectButton(frame.widget, 2, 2, 'Dwarf', 'Race', races, self.data)
        SelectButton(frame.widget, 3, 2, 'Elf', 'Race', races, self.data)

        ### Frame ###

        self.infolabel = Widgets(self.master, 1, 3)
        self.infolabel.label('')

        finalize = Widgets(self.master, 2, 3)
        finalize.button('Finalize', self.save)
        finalize.widget.configure(width = 10)

        cancel = Widgets(self.master, 0, 3)
        cancel.button('Cancel', self.master.destroy)
        cancel.widget.configure(width = 10)

    def save(self):
        name = self.nameselect.widget.get()
        race = self.data['Race']
        sex = self.data['Sex']
        if name == '':
            self.infolabel.widget.configure(text = 'Please select a Name')
        elif sex == None:
            self.infolabel.widget.configure(text = 'Please select a Sex')
        elif race == None:
            self.infolabel.widget.configure(text = 'Please select a Race')
        else:
            player.set_info(name, sex, race)
            player.set_all_attributes([5,5,5,5,5,5,5])
            player.set_all_attributes([0,0,0,0,0,0,0],1)
            player.languages = []
            player.languages.append(player.info['Race'])
            player.clear_inventory()
            datahandler.save()
            self.master.destroy()

class SelectButton(Widgets):
    def __init__(self, master, coulmn: int, row: int, text: str, type: str, list: list, data):
        super().__init__(master, coulmn, row)
        self.name = text
        self.button(text, lambda: self.command(type, list, data))
        self.widget.configure(width = 10)
        list.append(self)
        
    def command(self, type: str, list: list, data):
        data[type] = self.name
        for entry in list:
            if entry == int:
                pass
            elif entry.name != self.name:
                entry.widget.configure(state = 'active')
        self.widget.configure(state = 'disabled')
from .basic.menu import *
from ..assets.player import player

class PlayerCreation(Menu):
    def __init__(self):
        width = playercreationconfig['PlayerCreationWidth']
        height = playercreationconfig['PlayerCreationHeight']
        super().__init__(title = 'Character Creation', width = width, height = height)
        self.data = {
            'Race' : None,
            'Sex' : None
        }

    def open(self, master):
        super().open(master)
        line_padding1 = self.window.pad_line1
        line_padding2 = self.window.pad_line2
        center = self.window.center_x
        pad_opposite = self.window.pad_opposite
        pad = self.window.pad

        namelabel = Widgets(self.master, center, pad, 'n')
        namelabel.label('Choose your Name:')
        namelabel.widget.configure(justify='center')

        line2 = pad + line_padding1
        self.nameselect = Widgets(self.master, center, line2, 'n')
        self.nameselect.entry(20)
        self.nameselect.widget.configure(justify = 'center')

        line3 = line2 + line_padding2
        sex = []
        sexlabel = Widgets(self.master, center, line3, 'n')
        sexlabel.label('Choose your Sex:')
        sexlabel.widget.configure(justify='center')

        line4 = line3 + line_padding1
        SelectButton(self.master, center - 50, line4, 'n', 'Female', 'Sex', sex, self.data)
        SelectButton(self.master, center + 50, line4, 'n', 'Male', 'Sex', sex, self.data)

        line5 = line4 + line_padding2
        racelabel = Widgets(self.master, center, line5, 'n')
        racelabel.label('Choose your Race:')
        racelabel.widget.configure(justify='center')

        line6 = line5 + line_padding1
        races = []
        SelectButton(self.master, center - center/2, line6, 'n', 'Human', 'Race', races, self.data)
        SelectButton(self.master, center + center/2, line6, 'n', 'Dwarf', 'Race', races, self.data)
        SelectButton(self.master, center , line6, 'n', 'Elf', 'Race', races, self.data)

        line7 = line6 + line_padding2
        labelcontent = player.create_attributestring()
        attributelabel = Widgets(self.master, center + center/2, line7, 'ne')
        attributelabel.label(labelcontent)
        attributelabel.widget.configure(justify = 'left')

        labelcontent = player.create_attributevaluestring()
        attributelabel = Widgets(self.master, center + center/2, line7, 'nw')
        attributelabel.label(labelcontent)
        attributelabel.widget.configure(justify = 'left')

        self.infolabel = Widgets(self.master, center, pad_opposite - line_padding1, 's')
        self.infolabel.label('')
        finalize = Widgets(self.master, center, pad_opposite, 's')
        finalize.button('Finalize', self.save)

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
            player.save(name)
            self.master.destroy()

class SelectButton(Widgets):
    def __init__(self, master, x: int, y: int, anchor: str, text: str, type: str, list: list, data):
        super().__init__(master, x, y, anchor)
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
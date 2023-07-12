from .basic.menu import Menu
from app.resources.tkresource import Widgets
from app.resources.configuration.settings import playercreationconfig

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
        column1 = self.window.pad_left
        line1 = self.window.pad_top
        line_padding = self.window.pad_line
        center = self.window.center_x

        self.nameselect = Widgets(self.master, center, line1, 'nw')
        self.nameselect.entry(20)
        self.nameselect.widget.configure(justify = 'center')

        sex = []
        line2 = line1 + line_padding
        SelectButton(self.master, center - 50, line1 + 25, 'n', 'Female', 'Sex', sex, self.data)
        SelectButton(self.master, center + 50, line1 + 25, 'n', 'Male', 'Sex', sex, self.data)

        races = []
        line3 = line2 + line_padding
        SelectButton(self.master, center -100, line3, 'n', 'Human', 'Race', races, self.data)
        SelectButton(self.master, center +100, line3, 'n', 'Dwarf', 'Race', races, self.data)
        SelectButton(self.master, center , line3, 'n', 'Elf', 'Race', races, self.data)


        finalize = Widgets(self.master, self.window.center_x, self.window.pad_bottom, 's')
        finalize.button('Finalize', self.save)

    def save(self):
        name = self.nameselect.widget.get()
        race = self.data['Race']
        sex = self.data['Sex']
        print(name, race, sex)

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
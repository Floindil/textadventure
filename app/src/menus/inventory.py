from .basic.menu import Menu
from ..resources.configuration.settings import InventoryConfig
from ..resources.tkresource import Widgets
from ..assets.player import player

class Inventory(Menu):
    def __init__(self):
        width = InventoryConfig['Width']
        height = InventoryConfig['Height']
        title = 'Inventory'
        self.itemindex = 0
        super().__init__(title, width, height)

    def open(self, master):
        super().open(master)
        center = self.width/2

        ###################### Inventory Frame ######################

        frame = Widgets(self.master, center + center/2, self.height/2, 'center')
        frame.frame()

        left = Widgets(frame.widget, None, None, None)
        left.button('<', None)
        left.widget.pack(side = 'left')

        right = Widgets(frame.widget, None, None, None)
        right.button('>', None)
        right.widget.pack(side = 'right')

        self.itemlabel = Widgets(frame.widget, None, None, None)
        self.itemlabel.label(player.itemtypes[self.itemindex])
        self.itemlabel.widget.pack(side = 'top')

        items = self.load_items()
        itembox_width = InventoryConfig['Itembox_Width']
        itembox_lenght = InventoryConfig['Itembox_Height']
        self.itembox = Widgets(frame.widget, None, None, None)
        self.itembox.listbox(itembox_width, itembox_lenght, items)
        if len(items) > itembox_lenght:
            sb = Widgets(frame.widget, None, None, None)
            sb.scrollbar(self.itembox.widget)

        left.widget.configure(command = lambda: self.change_itemtype(0))
        right.widget.configure(command = self.change_itemtype)

        ###################### Inventory Frame ######################

        ###################### Equipment Frame ######################

        self.equipmentframe = Widgets(self.master, self.window.pad_line2, self.height/2, 'w')
        self.equipmentframe.frame()

        row = 0
        for slot in player.slots:
            self.unequip_button(slot, row)
            row +=1
        self.equipment_slots()

        ###################### Equipment Frame ######################

    def load_items(self):
        index = player.itemtypes[self.itemindex]
        items = player.items[index]
        list = []
        for item in items:
            list.append(item.name)
        return list
    
    def unequip(self, slot: str):
        if player.items['Equipment'][slot] == None:
            pass
        else:
            type = player.items['Equipment'][slot].type
            player.unequip(type, slot)
            new_content = self.load_items()
            self.itembox.change_lb_content(new_content)
            self.update_slots()
    
    def unequip_button(self, slot: str, row: int):
        button = Widgets(self.equipmentframe.widget, None, None, None)
        command = lambda: self.unequip(slot)
        button.button(slot, command)
        button.widget.configure(width = 10, padx = 5)
        button.widget.grid(column = 0, row = row, padx = 10)

    def return_equipped(self, slot: str):
        if player.items['Equipment'][slot] == None:
            equipped = ''
        else: 
            equipped = player.items['Equipment'][slot].name
        return equipped

    def equipment_slots(self):
        width = 25
        self.slots = []

        slot_armor = Widgets(self.equipmentframe.widget, None, None, None)
        armor = self.return_equipped('Armor')
        slot_armor.label(armor)
        slot_armor.widget.grid(column = 1, row = 0)
        slot_armor.widget.configure(width = width, bg = 'white', anchor = 'w', justify = 'left')
        self.slots.append((slot_armor.widget, 'Armor'))

        slot_right = Widgets(self.equipmentframe.widget, None, None, None)
        right = self.return_equipped('Right Hand')
        slot_right.label(right)
        slot_right.widget.grid(column = 1, row = 1)
        slot_right.widget.configure(width = width, bg = 'white', anchor = 'w', justify = 'left')
        self.slots.append((slot_right.widget, 'Right Hand'))

        slot_left= Widgets(self.equipmentframe.widget, None, None, None)
        left = self.return_equipped('Left Hand')
        slot_left.label(left)
        slot_left.widget.grid(column = 1, row = 2)
        slot_left.widget.configure(width = width, bg = 'white', anchor = 'w', justify = 'left')
        self.slots.append((slot_left.widget, 'Left Hand'))

        slot_talisman = Widgets(self.equipmentframe.widget, None, None, None)
        talisman = self.return_equipped('Talisman')
        slot_talisman.label(talisman)
        slot_talisman.widget.grid(column = 1, row = 3)
        slot_talisman.widget.configure(width = width, bg = 'white', anchor = 'w', justify = 'left')
        self.slots.append((slot_talisman.widget, 'Talisman'))

    def update_slots(self):
        for slot in self.slots:
            equipped = self.return_equipped(slot[1])
            slot[0].configure(text = equipped)
    
    def change_itemtype(self, direction: int = 1):
        if direction == 1:
            if self.itemindex == len(player.itemtypes )-1:
                self.itemindex = 0
            else: self.itemindex += 1
        elif direction == 0:
            if self.itemindex == 0:
                self.itemindex = len(player.itemtypes )-1
            else: self.itemindex -= 1
        key = player.itemtypes[self.itemindex]
        new_content = self.load_items()
        self.itembox.change_lb_content(new_content)
        self.itemlabel.widget.configure(text = key)

    def create_equipment(self):
        text = '\n'
        for key in player.items['Equipment']:
            text += '\n'
            equipped = player.items['Equipment'][key]
            if equipped == None:
                pass
            else:
                text += f'{equipped.name}'
        return text
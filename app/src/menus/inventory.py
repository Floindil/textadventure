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

        ### Equipment Frame {

        self.equipmentframe = Widgets(self.master, 0, 0)
        self.equipmentframe.frame()

        unequip_label = Widgets(self.equipmentframe.widget, 0, 0)
        unequip_label.pad = 0
        unequip_label.label('---Unequip---')

        equipped_label = Widgets(self.equipmentframe.widget, 1, 0)
        equipped_label.pad = 0
        equipped_label.label('-----------Equipped------------')

        row = 1
        for slot in player.slots:
            self.unequip_button(slot, row)
            row +=1
        self.equipment_slots()

        ### } Equipment Frame

        ### Inventory Frame {

        inventory_frame = Widgets(self.master, 0, 1)
        inventory_frame.frame()
        inventory_frame.widget.grid_anchor('center')
        inventory_frame.widget.grid(sticky = 'w')

        # Navigation Frame {

        navigation_frame = Widgets(inventory_frame.widget, 0, 0)
        navigation_frame.pad = 0
        navigation_frame.frame()

        left = Widgets(navigation_frame.widget, 0, 0)
        left.pad = 0
        left.button('<', None)

        right = Widgets(navigation_frame.widget, 2, 0)
        right.pad = 0
        right.button('>', None)

        self.itemlabel = Widgets(navigation_frame.widget, 1, 0)
        self.itemlabel.pad = 0
        self.itemlabel.label(player.itemtypes[self.itemindex])
        self.itemlabel.widget.configure(width = 15)

        # } Navigation Frame

        # Listbox Frame {

        listbox_frame = Widgets(inventory_frame.widget, 0, 1)
        listbox_frame.pad = 5
        listbox_frame.frame()

        items = self.load_items()
        itembox_width = InventoryConfig['Itembox_Width']
        itembox_lenght = InventoryConfig['Itembox_Height']
        self.itembox = Widgets(listbox_frame.widget, None, None)
        self.itembox.pad = 0
        self.itembox.listbox(itembox_width, itembox_lenght, items)
        if len(items) > itembox_lenght:
            sb = Widgets(listbox_frame.widget, None, None)
            sb.pad = 0
            sb.scrollbar(self.itembox.widget)

        # } Listbox Frame

        left.widget.configure(command = lambda: self.change_itemtype(0))
        right.widget.configure(command = self.change_itemtype)

        # Action Frame {
        
        action_frame = Widgets(inventory_frame.widget, 0, 2)
        action_frame.pad = 0
        action_frame.frame()

        self.action1 = Widgets(action_frame.widget,0,0)
        self.action1.pad = 0
        self.action1.button('Use', None)
        self.action1.widget.configure(width = 8)

        self.action2 = Widgets(action_frame.widget,1,0)
        self.action2.pad = 0
        self.action2.button('Discard', None)
        self.action2.widget.configure(width = 8)

        # } Equip Frame

        ### } Inventory Frame

        ### Player Information Frame {

        player_frame = Widgets(self.master, 1, 0)
        player_frame.frame()
        player_frame.widget.grid_anchor('w')

        # Info Frame {

        info_frame = Widgets(player_frame.widget, 0, 0)
        info_frame.pad = 0
        info_frame.frame()
        info_frame.widget.configure(bg = 'white')
        info_frame.widget.grid(sticky = 'nsew')

        infotext = player.list_dict(player.info)
        info = Widgets(info_frame.widget,  0, 0)
        info.label(infotext)
        info.widget.configure(justify = 'left', bg = 'white')
        info.widget.grid(sticky = 'w')

        valuetext = player.list_dict(player.info, 1)
        valuelabel = Widgets(info_frame.widget,  1, 0)
        valuelabel.label(valuetext)
        valuelabel.widget.configure(justify = 'left', bg = 'white')
        valuelabel.widget.grid(sticky = 'e')

        # } Info Frame

        # Attributes Frame {

        attributes_frame = Widgets(player_frame.widget, 0, 1)
        attributes_frame.pad = 0
        attributes_frame.frame()
        attributes_frame.widget.configure(bg = 'white')

        attribute_infotext = player.list_dict(player.attributes)
        attribute_infolabel = Widgets(attributes_frame.widget,  0, 0)
        attribute_infolabel.label(attribute_infotext)
        attribute_infolabel.widget.configure(justify = 'left', bg = 'white')

        attribute_valuetext = player.list_dict(player.attributes, 1)
        attribute_valuelabel = Widgets(attributes_frame.widget,  1, 0)
        attribute_valuelabel.label(attribute_valuetext)
        attribute_valuelabel.widget.configure(justify = 'right', bg = 'white')

        prefix_text = ''
        count = 0
        for value in player.attributbonuses:
            if player.attributbonuses[value] < 0:
                prefix_text += '-'
            else: prefix_text += '+'
            count +=1
            if count < len(player.attributbonuses):
                prefix_text += '\n'

        prefix_label = Widgets(attributes_frame.widget,  2, 0)
        prefix_label.pad =  0
        prefix_label.label(prefix_text)
        prefix_label.widget.configure(justify = 'center', bg = 'white')

        bonustext = player.list_dict(player.attributbonuses, 1)
        self.bonuslabel = Widgets(attributes_frame.widget,  3, 0)
        self.bonuslabel.label(bonustext)
        self.bonuslabel.widget.configure(justify = 'right', bg = 'white')

        # } Attributes Frame

        ### } Player Information Frame

    def bonuses_value_text(self):
        text = player.list_dict(player.attributbonuses, 1)
        return text

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
        button = Widgets(self.equipmentframe.widget, 0, row)
        command = lambda: self.unequip(slot)
        button.button(slot, command)
        button.widget.configure(width = 10, padx = 10)

    def return_equipped(self, slot: str):
        if player.items['Equipment'][slot] == None:
            equipped = ''
        else: 
            equipped = player.items['Equipment'][slot].name
        return equipped

    def equipment_slots(self):
        width = 25
        row = 1
        self.slots = []

        slot_armor = Widgets(self.equipmentframe.widget, 1, row)
        armor = self.return_equipped('Armor')
        slot_armor.label(armor)
        slot_armor.widget.configure(width = width, bg = 'white', justify = 'left')
        self.slots.append((slot_armor.widget, 'Armor'))

        slot_right = Widgets(self.equipmentframe.widget, 1, row+1)
        right = self.return_equipped('Right Hand')
        slot_right.label(right)
        slot_right.widget.configure(width = width, bg = 'white', justify = 'left')
        self.slots.append((slot_right.widget, 'Right Hand'))

        slot_left= Widgets(self.equipmentframe.widget, 1, row+2)
        left = self.return_equipped('Left Hand')
        slot_left.label(left)
        slot_left.widget.configure(width = width, bg = 'white', justify = 'left')
        self.slots.append((slot_left.widget, 'Left Hand'))

        slot_talisman = Widgets(self.equipmentframe.widget, 1, row+3)
        talisman = self.return_equipped('Talisman')
        slot_talisman.label(talisman)
        slot_talisman.widget.configure(width = width, bg = 'white', justify = 'left')
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
    
inventory = Inventory()
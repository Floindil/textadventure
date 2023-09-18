from .basic.menu import Menu
from ..resources.configuration.settings import InventoryConfig
from ..assets.data.inventorydata import Itemdata
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

        self.equipmentframe = Widgets(self.master)
        self.equipmentframe.frame('left')

        unequip_label = Widgets(self.equipmentframe.widget, 0, 0)
        unequip_label.pad = 0
        unequip_label.label('---Unequip---')

        equipped_label = Widgets(self.equipmentframe.widget, 1, 0)
        equipped_label.pad = 0
        equipped_label.label('-----------Equipped------------')

        row = 1
        for slot in player.equipment:
            self.unequip_button(slot, row)
            row +=1
        self.equipment_slots()

        ### } Equipment Frame

        ### Player Information Frame {

        player_frame = Widgets(self.master)
        player_frame.frame('right')
        player_frame.widget.grid_anchor('w')

        # Info Frame {

        info_frame = Widgets(player_frame.widget)
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

        attributes_frame = Widgets(player_frame.widget)
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

        ### Inventory Frame {

        inventory_frame = Widgets(self.master)
        inventory_frame.frame()
        inventory_frame.widget.grid_anchor('center')
        inventory_frame.widget.grid(sticky = 'w')

        # Navigation Frame {

        navigation_frame = Widgets(inventory_frame.widget)
        navigation_frame.pad = 0
        navigation_frame.frame()

        left = Widgets(navigation_frame.widget, 0, 0)
        left.pad = 0
        left.button('<', self.change_left)

        right = Widgets(navigation_frame.widget, 2, 0)
        right.pad = 0
        right.button('>', self.change_right)

        self.itemlabel = Widgets(navigation_frame.widget, 1, 0)
        self.itemlabel.pad = 0
        self.itemlabel.label(player.itemtypes[self.itemindex])
        self.itemlabel.widget.configure(width = 15)

        # } Navigation Frame

        # Listbox Frame {

        listbox_frame = Widgets(inventory_frame.widget)
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
        self.itembox.widget.bind('<<ListboxSelect>>', self.set_index)

        # } Listbox Frame

        # Action Frame {
        
        action_frame = Widgets(inventory_frame.widget)
        action_frame.pad = 0
        action_frame.frame()

        self.action1 = Widgets(action_frame.widget,0,0)
        self.action1.pad = 0
        self.action1.button('Use', None)
        self.action1.widget.configure(width = 8)

        self.action2 = Widgets(action_frame.widget,1,0)
        self.action2.pad = 0
        self.action2.button('TBD', None)
        self.action2.widget.configure(width = 8)

        # } Equip Frame

        # Iteminformation Frame {
        
        iteminformation_frame = Widgets(inventory_frame.widget)
        iteminformation_frame.pad = 0
        iteminformation_frame.frame()
        iteminformation_frame.widget.grid(sticky = 'nsew')

        self.item_infolabel = Widgets(iteminformation_frame.widget, 0, 0)
        text = ''
        self.item_infolabel.label(text)

        # } Iteminformation Frame

        ### } Inventory Frame      

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
    
    def set_index(self, event = None):
        self.index = self.itembox.widget.curselection()
        self.change_itemdescription()
    
    def get_itemdescription(self):
        itemname = self.itembox.widget.get(self.index)
        item = self.get_item_from_name(itemname)
        text = item.description
        return text
    
    def change_itemdescription(self):
        if self.index != None:
            text = self.get_itemdescription()
        else: text = 'select item'
        self.item_infolabel.widget.configure(text = text)
    
    def get_item_from_name(self, name: str):
        itemtype = player.itemtypes[self.itemindex]
        for item in player.items[itemtype]:
            if item.name == name:
                return item
    
    def equip(self):
        target_equipable = self.itembox.widget.get(self.index)
        item = self.get_item_from_name(target_equipable)
        target_slot = player.equipment[item.slot[0]]
        if target_slot != None:
            target_slot.unequip()
        item.equip()
        new_content = self.load_items()
        self.itembox.change_lb_content(new_content)
        self.index = None
        self.change_itemdescription()
        self.update_slots()
        Itemdata.dump()

    def unequip(self, slot: str):
        if player.equipment[slot] == None:
            pass
        else:
            item = player.equipment[slot]
            item.unequip()
            new_content = self.load_items()
            self.itembox.change_lb_content(new_content)
            self.update_slots()
            Itemdata.dump()
    
    def unequip_button(self, slot: str, row: int):
        button = Widgets(self.equipmentframe.widget, 0, row)
        command = lambda: self.unequip(slot)
        button.button(slot, command)
        button.widget.configure(width = 10, padx = 10)

    def return_equipped(self, slot: str):
        if player.equipment[slot] == None:
            equipped = ''
        else: 
            equipped = player.equipment[slot].name
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
        right = self.return_equipped('First Hand')
        slot_right.label(right)
        slot_right.widget.configure(width = width, bg = 'white', justify = 'left')
        self.slots.append((slot_right.widget, 'First Hand'))

        slot_left= Widgets(self.equipmentframe.widget, 1, row+2)
        left = self.return_equipped('Second Hand')
        slot_left.label(left)
        slot_left.widget.configure(width = width, bg = 'white', justify = 'left')
        self.slots.append((slot_left.widget, 'Second Hand'))

        slot_talisman = Widgets(self.equipmentframe.widget, 1, row+3)
        talisman = self.return_equipped('Talisman')
        slot_talisman.label(talisman)
        slot_talisman.widget.configure(width = width, bg = 'white', justify = 'left')
        self.slots.append((slot_talisman.widget, 'Talisman'))

    def update_slots(self):
        for slot in self.slots:
            equipped = self.return_equipped(slot[1])
            slot[0].configure(text = equipped)

    def update_command(self):
        key = player.itemtypes[self.itemindex]
        if self.itemindex > 1: # last use command in commands
            type = player.itemtypes[self.itemindex]
            if type == 'Twohanded':
                type = 'First Hand'
            command = self.equip
            text = 'Equip'
        else: 
            command = None
            text = 'Use'
        self.action1.widget.configure(command = command, text = text)
        self.itemlabel.widget.configure(text = key)
    
    def change_itemtype(self):
        self.update_command()
        new_content = self.load_items()
        self.itembox.change_lb_content(new_content)

    def change_left(self):
        if self.itemindex == 0:
            self.itemindex = len(player.itemtypes)-1
        else: self.itemindex -= 1
        self.change_itemtype()

    def change_right(self):
        if self.itemindex == len(player.itemtypes)-1:
            self.itemindex = 0
        else: self.itemindex += 1
        self.change_itemtype()

    def create_equipment(self):
        text = '\n'
        for key in player.equipment:
            text += '\n'
            equipped = player.equipment[key]
            if equipped == None:
                pass
            else:
                text += f'{equipped.name}'
        return text
    
inventory = Inventory()
from .sources.character import Character
from .sources.inventory import Inventory
from .sources.equipment import Equipment
from .sources.attributes import Attributes
from .sources.statistics import Statistics
from ..names_values import player

class Player:
    player={
            player[0]:None,
            player[1]:None,
            player[2]:None,
            player[3]:None,
            player[4]:None
        }
### Player ###
    @classmethod
    def update_player(cls):
        for part in cls.player:
            cls.player.update({part:cls.return_part(part)})
    
    @classmethod
    def return_part(cls,part:str):
        if part==player[0]:
            return cls.return_character()
        elif part==player[1]:
            return cls.return_items()
        elif part==player[2]:
            return cls.return_equipment()
        elif part==player[3]:
            return cls.return_attributes()
        elif part==player[4]:
            return cls.return_statistics()
    
### Character ###
    @staticmethod
    def return_character():
        return Character.character

    @staticmethod
    def get_character(dict:dict):
        Character.get_character(dict=dict)

### Inventory ###
    @staticmethod
    def add_item(item:str,type:str):
        Inventory.add_item(item=item,type=type)

    @staticmethod
    def remove_item(item:str,type:str):
        Inventory.remove_item(item=item,type=type)

    @staticmethod
    def return_items():
        return Inventory.items

    @staticmethod
    def get_items(data:dict):
        Inventory.get_items(data)

### Equipment ###
    @staticmethod
    def equip(item,slot:str):
        if Player.return_equipped(slot=slot):
            Player.unequip(slot)
        Inventory.remove_item(item=item,type=item.type)
        Equipment.equip(item=item,slot=slot)

    @staticmethod
    def unequip(slot:str):
        equipped=Player.return_equipped(slot=slot)
        Inventory.add_item(item=equipped,type=equipped.type)
        Equipment.unequip(slot=slot)

    @staticmethod
    def return_equipment():
        return Equipment.equipment

    @staticmethod
    def return_equipped(slot:str):
        return Equipment.equipment.get(slot)

    @staticmethod
    def get_equipment(dict:dict):
        Equipment.get_equipment(dict=dict)

### Attributes ###
    @staticmethod
    def change_attributes(change_list:list=[0,1,2,3,4,5,6]):
        Attributes.change(change_list)

    @staticmethod
    def return_attributes():
        return Attributes.attributes
    
    @staticmethod
    def get_attributes(dict:dict):
        Attributes.get_attributes(dict=dict)

### Statistics ###
    @staticmethod
    def update_statistics():
        Statistics.update_statistics()
    
    @staticmethod
    def update_value(type:int,value:int):
        Statistics.update_value(type=type,value=value)

    @staticmethod
    def return_statistics():
        return Statistics.statistics
    
    @staticmethod
    def recover_value(type:int):
        Statistics.recover_value(type=type)

    def recover_full():
        Statistics.recover_full()
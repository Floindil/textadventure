from .sources.character import Character
from .sources.inventory import Inventory
from .sources.equipment import Equipment
from .sources.naming import player

class Player:
    player={
            player[0]:None,
            player[1]:None,
            player[2]:None
        }
### Player ###
    @classmethod
    def create_player(cls):
        for part in cls.player:
            cls.player.update({part:cls.return_part(part)})

    @classmethod
    def return_player(cls):
        return cls.player
    
    @classmethod
    def return_part(cls,part:str):
        if part==player[0]:
            return cls.return_character()
        elif part==player[1]:
            return cls.return_items()
        elif part==player[2]:
            return cls.return_equipment()
    
### Character ###
    @staticmethod
    def return_character():
        return Character.return_character()

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
        return Inventory.return_items()

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
        return Equipment.return_equipment()

    @staticmethod
    def return_equipped(slot:str):
        return Equipment.equipment.get(slot)

    @staticmethod
    def get_equipment(dict:dict):
        Equipment.get_equipment(dict=dict)
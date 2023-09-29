from .sources.character import Character as C
from .sources.inventory import Inventory as I
from .sources.equipment import Equipment as E
from .sources.attributes import Attributes as A
from .sources.statistics import Statistics as S
from .sources.resources import Resources as R
from ..names_values import player

class Player:
    player= {
            player[0]: None,
            player[1]: None,
            player[2]: None,
            player[3]: None,
            player[4]: None,
            player[5]: None
        }
### Player ###
    @classmethod
    def update_player(cls):
        for part in cls.player:
            cls.player.update({part: cls.return_part(part)})
    
    @classmethod
    def return_part(cls, part: str):
        if part== player[0]:
            return cls.return_character()
        elif part== player[1]:
            return cls.return_items()
        elif part== player[2]:
            return cls.return_equipment()
        elif part== player[3]:
            return cls.return_attributes()
        elif part== player[4]:
            cls.update_statistics()
            return cls.return_statistics()
        elif part== player[5]:
            return cls.return_resources()
    
### Character ###
    @staticmethod
    def return_character():
        return C.character

    @staticmethod
    def get_character(dict: dict):
        C.get_character(dict= dict)

### Inventory ###
    @staticmethod
    def add_item(item: str):
        I.add_item(item= item)

    @staticmethod
    def remove_item(item: str):
        I.remove_item(item= item)

    @staticmethod
    def return_items():
        return I.items
    
    @staticmethod
    def return_itemnames():
        item_dict= {}
        for key in I.items:
            items=I.items.get(key)
            name_list= []
            for item in items:
                name_list.append(item.name)
            item_dict.update({key: name_list})
        return item_dict
            

    @staticmethod
    def get_items(data: dict):
        I.get_items(data)

### Equipment ###
    @staticmethod
    def equip(item, slot: str):
        if Player.return_equipped(slot= slot):
            Player.unequip(slot)
        I.remove_item(item= item, type= item.type)
        E.equip(item= item, slot= slot)

    @staticmethod
    def unequip(slot: str):
        equipped= Player.return_equipped(slot= slot)
        I.add_item(item= equipped, type= equipped.type)
        E.unequip(slot= slot)

    @staticmethod
    def return_equipment():
        return E.equipment

    @staticmethod
    def return_equipped(slot: str):
        return E.equipment.get(slot)

    @staticmethod
    def get_equipment(dict: dict):
        E.get_equipment(dict= dict)

### Attributes ###
    @staticmethod
    def update_attribute(type: str, value: int):
        A.update_attribute(type= type, value= value)

    @staticmethod
    def update_attributes(change_list: list= [0, 1, 2, 3, 4, 5, 6]):
        A.update(change_list)

    @staticmethod
    def return_attributes():
        return A.attributes
    
    @staticmethod
    def get_attributes(dict: dict):
        A.get_attributes(dict= dict)

### Statistics ###
    @staticmethod
    def update_statistics():
        S.update_statistics()
    
    @staticmethod
    def update_statvalue(type: int, value: int):
        S.update_value(type= type, value= value)

    @staticmethod
    def return_statistics():
        return S.statistics
    
    @staticmethod
    def recover_value(type: int):
        S.recover_value(type= type)
        
    @staticmethod
    def recover_full():
        S.recover_full()
        
### Resources###
    @staticmethod
    def update_currency(value: int):
        R.update_resource(value= value, resource= 0)
        
    @staticmethod
    def update_exp(value: int):
        R.update_resource(value= value, resource= 1)
        
    @staticmethod
    def return_resources():
        return R.resources
    
### Items ###
    @staticmethod
    def use_item(item):
        if item.affected in S.statistics:
            Player.update_statvalue(type= item.affected, value= item.value)
        elif item.affected in A.attributes:
            Player.update_attribute(type= item.affected, value= item.value)
        Player.remove_item(item)
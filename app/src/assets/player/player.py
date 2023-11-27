from .sources.character import Character as C
from .sources.inventory import Inventory as I
from .sources.equipment import Equipment as E
from .sources.resources import Resources as R
from .sources.attributes import Attributes as A
from .sources.statistics import Statistics as S
from .sources.buffs import Buffs as B
from ..names_values import player as p, attributes as a
'''
Values imported from names_values file are only stated there to allow easy name changes late in the project
'''
class Player:
    player= {
            p[0]: None,
            p[1]: None,
            p[2]: None,
            p[3]: None,
            p[4]: None,
            p[5]: None,
            p[6]: None
        }
#region Player
    @classmethod
    def update_player(cls):
        for part in cls.player:
            cls.player.update({part: cls.return_part(part)})
    
    @classmethod
    def return_part(cls, part: str):
        if part== p[0]:
            return cls.return_character()
        elif part== p[1]:
            return cls.return_items()
        elif part== p[2]:
            return cls.return_equipment(), cls.return_equipment_values()
        elif part== p[3]:
            return cls.return_attributes()
        elif part== p[4]:
            cls.update_statistics()
            return cls.return_statistics(), cls.return_statistics_values()
        elif part== p[5]:
            return cls.return_resources()
        elif part== p[6]:
            return cls.return_buffs(), cls.return_buff_values()
    #endregion
    
#region Character
    @staticmethod
    def return_character():
        return C.character

    @staticmethod
    def get_character(dict: dict):
        C.get_character(dict= dict)
    #endregion

#region Inventory
    @staticmethod
    def add_item(item, amount: int= 1):
        I.add_item(item= item, amount= amount)

    @staticmethod
    def remove_item(item, amount: int= 1):
        I.remove_item(item= item, amount= amount)

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
    #endregion

#region Equipment
    @staticmethod
    def equip(item):
        check = Player.check_requirements(item=item)
        if check:
            for slot in item.slots:
                if Player.return_equipped(slot= slot):
                    Player.unequip(slot)
            if item.buff:
                Player.update_buff(item.buff)
            Player.remove_item(item= item)
            E.equip(item= item)
            return True
        else: return False

    @staticmethod
    def unequip(slot: str): 
        equipped= Player.return_equipped(slot= slot)
        Player.add_item(item= equipped)
        if equipped.buff:
            Player.update_buff(equipped.buff, remove = True)
        E.unequip(slot= slot)

    @staticmethod
    def check_requirements(item):
        if not item.requirements: return True
        index= 0
        attributes= Player.return_attributes()
        buff_values = Player.return_buff_values()
        for requirement in item.requirements:
            attribute= attributes.get(a[index]) + buff_values.get(a[index])
            index+= 1
            if requirement> attribute:
                return False
        return True

    @staticmethod
    def return_equipment():
        return E.equipment
    
    @staticmethod
    def return_equipment_values():
        return E.values

    @staticmethod
    def return_equipped(slot: str):
        return E.equipment.get(slot)

    @staticmethod
    def get_equipment(dict: dict):
        E.get_equipment(dict= dict)
    #endregion

#region Attributes
    @staticmethod
    def update_attribute(type: str, value: int):
        A.update_attribute(type= type, value= value)

    @staticmethod
    def update_attributes(change_list: list= [0, 1, 2, 3, 4, 5, 6]):
        A.update(change_list)

    @staticmethod
    def return_attributes():
        return A.values
    
    @staticmethod
    def get_attributes(dict: dict):
        A.get_attributes(dict= dict)
    #endregion

#region Statistics
    @staticmethod
    def update_statistics():
        S.update_statistics()
    
    @staticmethod
    def update_statvalue(type: int, value: int):
        S.update_value(type= type, value= value)

    @staticmethod
    def return_statistics():
        return S.statistics
    
    def return_statistics_values():
        return S.values
    
    @staticmethod
    def recover_value(type: int):
        S.recover_value(type= type)
        
    @staticmethod
    def recover_full():
        S.recover_full()
    #endregion
        
#region Resources
    @staticmethod
    def update_currency(value: int):
        R.update_resource(value= value, resource= 0)
        
    @staticmethod
    def update_exp(value: int):
        R.update_resource(value= value, resource= 1)
        
    @staticmethod
    def return_resources():
        return R.resources
    #endregion
    
#region Items
    @staticmethod
    def use_item(item):
        for effect in item.effect:
            if effect[0] in S.statistics:
                Player.update_statvalue(type= effect[0], value= effect[1])
            elif effect[0] in A.values:
                Player.update_attribute(type= effect[0], value= effect[1])
                Player.update_statistics()
        Player.remove_item(item)
    #endregion

#region Buffs
    @staticmethod
    def return_buffs():
        return B.buffs

    @staticmethod
    def return_buff_values():
        return B.values
    
    def update_buff(buff: dict, remove: bool = False):
        B.update_buff(buff = buff, remove = remove)
        types = buff.get('type')
        for t in types:
            if t in Player.player.get(p[2])[1]:
                pass
            else:
                Player.update_statistics()
    #endregion
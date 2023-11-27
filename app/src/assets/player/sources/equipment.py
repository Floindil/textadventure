from ...names_values import equipment as e, equipment_values as ev
from .buffs import Buffs as B
'''
Values imported from names_values file are only stated there to allow easy name changes late in the project
'''
class Equipment:
    equipment= {
        e[0]: None,
        e[1]: None,
        e[2]: None,
        e[3]: None
    }
    values= {
        ev[0]: 0,
        ev[1]: 0,
        ev[2]: 0,
        ev[3]: 0,
        ev[4]: 0
    }

    @classmethod
    def equip(cls, item):
        for slot in item.slots:
            if cls.equipment.get(slot): cls.unequip(slot= slot)
            cls.equipment.update({slot: item})
        if item.values:
            cls.update_values(values = item.values)

    @classmethod
    def unequip(cls, slot: str):
        item= cls.equipment.get(slot)
        if item.values:
            cls.update_values(values = item.values, remove= True)
        for s in item.slots:
            cls.equipment.update({s: None})
    
    @classmethod
    def get_equipment(cls, dict: dict):
        for slot in cls.equipment:
            value = dict.get(slot)
            cls.equipment.update({slot: value})

    @classmethod
    def update_value(cls, type:str, value:int):
        new_value = cls.values.get(type) + B.values.get(type) + value
        cls.values.update({type: new_value})

    @classmethod
    def update_values(cls, values: list = [0, 1, 2, 3, 4], remove: bool = False):
        index = 0
        for value in cls.values:
            current = cls.values.get(value)
            if not remove: new = current+ values[index]
            else: new = current - values[index]
            cls.values.update({value: new})
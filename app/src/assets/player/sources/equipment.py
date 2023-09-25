from ...names_values import equipment as e

class Equipment:
    equipment={
        e[0]:None,
        e[1]:None,
        e[2]:None,
        e[3]:None
    }

    @classmethod
    def equip(cls, item, slot:str):
        cls.equipment.update({slot:item})

    @classmethod
    def unequip(cls, slot):
        cls.equipment.update({slot:None})
    
    @classmethod
    def get_equipment(cls, dict:dict):
        for slot in cls.equipment:
            value=dict.get(slot)
            cls.equipment.update({slot:value})
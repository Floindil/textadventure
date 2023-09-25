from ...fixed_values import equipment

class Equipment:
    equipment={
        equipment[0]:None,
        equipment[1]:None,
        equipment[2]:None,
        equipment[3]:None
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
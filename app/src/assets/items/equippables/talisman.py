from .basic.equipable import Equipable
from ...names_values import equipment as e, items as i, statistics as s

class Talisman(Equipable):
    '''values: Armor, Attack, Block, Range, Accuracy
    buffs: [[attribute1, attribute2], [value1, value2]]
    requirements: Body, Agility, Strenght, Dexterity, Intelligence, Light Magic, Dark Magic'''
    def __init__(self, name: str, values: list, buff: dict= None, requirements: list= None) -> None:
        super().__init__(
            name = name,
            slots = [e[3]],
            values = values,
            buff = buff,
            requirements = requirements
        )
        self.type= i[3]

    @classmethod
    def h_talisman(cls):
        return cls(
            name = 'Health Talisman',
            values = None,
            buff = [
                [s[0]],
                [10]
            ] 
        )
    
    @classmethod
    def s_talisman(cls):
        return cls(
            name = 'Stamina Talisman',
            values = None,
            buff = [
                [s[1]],
                [5]
            ] 
        )
from .basic.equipable import Equipable
from ...names_values import equipment as e, items as i

class Sword(Equipable):
    '''values: Armor, Attack, Block, Range, Accuracy
    buffs: [[attribute1, attribute2], [value1, value2]]
    requirements: Body, Agility, Strenght, Dexterity, Intelligence, Light Magic, Dark Magic'''
    def __init__(self, name: str, values: list, buff: dict= None, requirements: list= None) -> None:
        super().__init__(
            name = name,
            slots = [e[0]],
            values = values,
            buff = buff,
            requirements = requirements
        )
        self.type= i[1]

    @classmethod
    def swordusLongus(cls):
        return cls(
            name = 'Iron Shortsword',
            values = [0, 4, 2, 2, 9]
        )

    @classmethod
    def swordusBiggus(cls):
        return cls(
            name = 'Steel Shortsword',
            values = [0, 8, 2, 2, 9],
            requirements = [0, 10, 0, 0, 0, 0, 0]
        )
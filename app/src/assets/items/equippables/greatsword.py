from .basic.equipable import Equipable
from ...names_values import equipment as e, items as i

class Greatsword(Equipable):
    '''values: Armor, Attack, Block, Range, Accuracy
    buffs: [[attribute1, attribute2], [value1, value2]]
    requirements: Body, Agility, Strenght, Dexterity, Intelligence, Light Magic, Dark Magic'''
    def __init__(self, name: str, values: list, buff: dict= None, requirements: list= None) -> None:
        super().__init__(
            name = name,
            slots = [e[0], e[1]],
            values = values,
            buff = buff,
            requirements = requirements
        )
        self.type= i[1]

    @classmethod
    def swordusBiggustest(cls):
        return cls(
            name = 'Iron Greatsword',
            values = [0, 15, 2, 3, 9]
        )
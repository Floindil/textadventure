from .basic.equipable import Equipable
from ...names_values import equipment as e, items as i

class Shield(Equipable):
    '''values: Armor, Attack, Block, Range, Accuracy
    buff: {attribute1: value1, attribute2: value2}
    requirements: Body, Agility, Strenght, Dexterity, Intelligence, Light Magic, Dark Magic'''
    def __init__(self, name: str, values: list, buff: dict= None, requirements: list= None) -> None:
        super().__init__(
            name = name,
            slots = [e[1]],
            values = values,
            buff = buff,
            requirements = requirements
        )
        self.type= i[2]

    @classmethod
    def i_shield(cls):
        return cls(
            name = 'Iron Shield',
            values = [5, 0, 5, 0, 9]
        )
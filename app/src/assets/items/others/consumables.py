from ...names_values import items as i, statistics as s, attributes as a
from .basic.item import Item
'''
Values imported from names_values file are only stated there to allow easy name changes late in the project
'''
class Consumables(Item):
    
    def __init__(self, name: str, effect: list, duration: int=0) -> None:
        '''effect list: [(affected1, value1), (affected2, value2), ...]'''
        super().__init__(name)
        self.type= i[0]
        self.name= name
        self.effect= effect
        self.duration= duration

    @classmethod
    def apple(cls):
        return cls(
            name = 'Apple',
            effect = [(s[0], 10)]
        )
    
    @classmethod
    def healthpotion(cls):
        return cls(
            name = 'Health Potion',
            effect = [(s[0]), 20]
        )
    
    @classmethod
    def staminapotion(cls):
        return cls(
            name = 'Stamina Potion',
            effect = [(s[1]), 20]
        )
    
    @classmethod
    def manapotion(cls):
        return cls(
            name = 'Mana Potion',
            effect = [(s[1]), 20]
        )
    
    @classmethod
    def drugs(cls):
        return cls(
            name = 'Drugs',
            effect = [(a[1], -2)]
        )
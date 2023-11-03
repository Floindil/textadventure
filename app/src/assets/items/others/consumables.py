from ...names_values import items as i, statistics as s
from .basic.item import Item

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
        return cls('Apple',[(s[0], 10)])
    
    @classmethod
    def healthpotion(cls):
        return cls('Health Potion', [(s[0]), 20])
    
    @classmethod
    def staminapotion(cls):
        return cls('Stamina Potion', [(s[1]), 20])
    
    @classmethod
    def manapotion(cls):
        return cls('Mana Potion', [(s[1]), 20])
    
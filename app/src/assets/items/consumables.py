from ...names_values import items as i
from .basic.item import Item

class Consumables(Item):
    
    def __init__(self, name: str, effect: list, duration: int=0) -> None:
        '''effect list: [(affected1, value1), (affected2, value2), ...]'''
        super().__init__(name)
        self.type= i[0]
        self.name= name
        self.effect= effect
        self.duration= duration
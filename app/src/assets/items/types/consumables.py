from ...names_values import items as i
from .basic.item import Item

class Consumables(Item):
    def __init__(self, name: str, affects: int, value: int, duration: int=0) -> None:
        super().__init__(name)
        self.type= i[0]
        self.name= name
        self.affected= affects
        self.value= value
        self.duration= duration
from ...names_values import items as i
from .basic.item import Item

class Keyitems(Item):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type= i[4]
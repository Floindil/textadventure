from ...names_values import items as i
from .basic.item import Item

class Keyitems(Item):
    def __init__(self,name:str) -> None:
        self.type = i[4]
        self.name=name

    def find(self):
        self.add()
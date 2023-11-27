from ...names_values import items as i
from .basic.item import Item
'''
Values imported from names_values file are only stated there to allow easy name changes late in the project
'''
class Materials(Item):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type= i[5]
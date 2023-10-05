from .basic.equipable import Equipable
from ..names_values import equipment as e, items as i

class Shield(Equipable):
    def __init__(self, name: str, values: list, requirements: list= None) -> None:
        super().__init__(name, [e[1]], values, requirements)
        self.type= i[2]
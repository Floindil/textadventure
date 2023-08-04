from .basic.item import Item
from ...player import player

class Consumable(Item):
    def __init__(self, name: str, description: str, value: int, attributes: list) -> None:
        super().__init__(name, description, value, attributes)
        self.type = 'Consumables'

    def use(self):
        player.change_attributese(self.attributes, self.value)
        player.remove_item(self, self.type)

class Keyitem(Item):
    def __init__(self, name: str, description: str, value: int, attributes: list) -> None:
        super().__init__(name, description, value, attributes)
        self.type = 'Keyitems'

class Equipable(Item):
    def __init__(self, name: str, description: str, value: int, attributes: list = [({'attribute': str,'requirement': int})]) -> None:
        super().__init__(name, description, value, attributes)

    def equip(self):
        player.equip(self, self.type, self.slot[0])

    def unequip(self):
        player.unequip(self.type, self.slot[0])

    def check_requirements(self):
        index = 0
        checks = []
        for attribut in self.attributes:
            if self.attributes[index][1] < player.info[attribut[0]]:
                checks.append((attribut[0], False))
            else: checks.append((attribut[0], True))
            index +=1
        return checks

class Armor(Equipable):
    def __init__(self, name: str, description: str, value: int, attributes: list = [({'attribute': str,'requirement': int})]) -> None:
        super().__init__(name, description, value, attributes)
        self.type = 'Armor'
        self.slot = [self.type]
    
class Shield(Armor):
    def __init__(self, name: str, description: str, value: int, attributes: list = [{ 'attribute': str,'requirement': int }]) -> None:
        super().__init__(name, description, value, attributes)
        self.slot = ['Second Hand']

class Talisman(Equipable):
    def __init__(self, name: str, description: str, value: int, attributes: list = [({'attribute': str,'requirement': int})]) -> None:
        super().__init__(name, description, value, attributes)
        self.type = 'Talisman'
        self.slot = [self.type]
from .basic.item import Item
from ...player import player

class Consumable(Item):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'Consumables'

    def use(self):
        player.change_attribute(self.attribut, self.value)
        player.remove_item(self, self.type)

class Keyitem(Item):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'Keyitems'

class Equipable(Item):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)

    def equip(self):
        player.equip(self, self.type, self.slot)

    def unequip(self):
        player.unequip(self.type, self.slot)

class Weapon(Equipable):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'Weapons'
        self.slot = {
            0 : 'Right Hand',
            1 : 'Left Hand'
        }

    def equip(self, slot):
        player.equip(self, self.type, self.slot[slot])

    def unequip(self, slot):
        player.unequip(self.type, self.slot[slot])

class Armor(Equipable):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'Armor'
        self.slot = self.type

class Talisman(Equipable):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'Talisman'
        self.slot = self.type
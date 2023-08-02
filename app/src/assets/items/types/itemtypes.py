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

class On_Hand(Equipable):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'On-Hand'
        self.slot = self.type

class Off_Hand(Equipable):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'Off-Hand'
        self.slot = self.type

class Twohanded(Equipable):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'Twohanded'
        self.slot = ['On-Hand', 'Off-Hand']

    def equip(self):
        player.equip(self, self.type, self.slot[0])
        player.add_item(self, self.type)
        player.equip(self, self.type, self.slot[1])

    def unequip(self):
        player.unequip(self.type, self.slot[0])
        player.remove_item(self, self.type)
        player.unequip(self.type, self.slot[1])
        

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
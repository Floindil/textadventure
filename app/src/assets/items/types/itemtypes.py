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
        player.equip(self, self.type, self.slot[0])

    def unequip(self):
        player.unequip(self.type, self.slot[0])

class On_Hand(Equipable):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'Weapons'
        self.slot = ['First Hand']

class Bow(On_Hand):
    pass

class Off_Hand(Equipable):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'Weapons'
        self.slot = ['Second Hand']

class Arrow(Off_Hand):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.amount = 0
        self.setname = name
        self.name = f'{self.setname} (x{self.amount})'

    def get_more(self, amount):
        if amount > self.amount: self.amount = 0
        else: self.amount += amount
        self.name = f'{self.setname} (x{self.amount})'

class Twohanded(Equipable):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'Weapons'
        self.slot = ['First Hand', 'Second Hand']

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
        self.slot = [self.type]

class Talisman(Equipable):
    def __init__(self, name: str, description: str, value: int, attribut: str) -> None:
        super().__init__(name, description, value, attribut)
        self.type = 'Talisman'
        self.slot = [self.type]
from .itemtypes import Equipable, player

class On_Hand(Equipable):
    def __init__(self, name: str, description: str, value: int, attributes: list = [({'attribute': str,'requirement': int})]) -> None:
        super().__init__(name, description, value, attributes)
        self.type = 'Weapons'
        self.slot = ['First Hand']
        self.damage = self.value*self.attributes

    def hit(self, target):
        target.hp -= self.damage

class Sword(On_Hand):
    def __init__(self, name: str, description: str, value: int, attributes: list = [{ 'attribute': str,'requirement': int }]) -> None:
        super().__init__(name, description, value, attributes)
        self.weapontype = 'Sword'

class DaggerH1(On_Hand):
    def __init__(self, name: str, description: str, value: int, attributes: list = [{ 'attribute': str,'requirement': int }]) -> None:
        super().__init__(name, description, value, attributes)
        self.weapontype = 'Dagger'

class Bow(On_Hand):
    def __init__(self, name: str, description: str, value: int, attributes: list) -> None:
        super().__init__(name, description, value, attributes)
        self.weapontype = 'Bow'

class Off_Hand(Equipable):
    def __init__(self, name: str, description: str, value: int, attributes: list = [({'attribute': str,'requirement': int})]) -> None:
        super().__init__(name, description, value, attributes)
        self.type = 'Weapons'
        self.slot = ['Second Hand']

class DaggerH2(Off_Hand):
    def __init__(self, name: str, description: str, value: int, attributes: list = [{ 'attribute': str,'requirement': int }]) -> None:
        super().__init__(name, description, value, attributes)
        self.weapontype = 'Dagger'

class Arrow(Off_Hand):
    def __init__(self, name: str, description: str, value: int, attributes: list) -> None:
        super().__init__(name, description, value, attributes)
        self.weapontype = 'Arrow'
        self.amount = 0
        self.setname = name
        self.name = f'{self.setname} (x{self.amount})'

    def get_more(self, amount):
        if amount > self.amount: self.amount = 0
        else: self.amount += amount
        self.name = f'{self.setname} (x{self.amount})'

class Twohanded(Equipable):
    def __init__(self, name: str, description: str, value: int, attributes: list = [({'attribute': str,'requirement': int})]) -> None:
        super().__init__(name, description, value, attributes)
        self.type = 'Weapons'
        self.slot = ['First Hand', 'Second Hand']
        self.damage = self.value*self.attributes

    def equip(self):
        player.equip(self, self.type, self.slot[0])
        player.add_item(self, self.type)
        player.equip(self, self.type, self.slot[1])

    def unequip(self):
        player.unequip(self.type, self.slot[0])
        player.remove_item(self, self.type)
        player.unequip(self.type, self.slot[1])

class Greatsword(Twohanded):
    def __init__(self, name: str, description: str, value: int, attributes: list = [{ 'attribute': str,'requirement': int }]) -> None:
        super().__init__(name, description, value, attributes)
        self.weapontype = 'Greatsword'
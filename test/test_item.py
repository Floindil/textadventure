from methods import Test
from setup import set_testplayer
from app.src.assets.items.itemlist import *

class TestItem(Test):
    def test_item(self):
        set_testplayer()
        self.add_all_items()

        self.use_item(apple)
        self.use_item(poisonedapple)

        self.create_summary()
        print(self.summary)

    def test_equipment(self):

        set_testplayer()
        self.add_all_items()

        leatherarmor.equip()
        sword.equip()
        shield.equip()

        self.create_summary()
        print(self.summary)
        print('')

        leatherarmor.unequip()
        sword.unequip()
        shield.unequip()

        self.create_summary()
        print(self.summary)
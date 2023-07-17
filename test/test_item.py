from methods import Test
from app.src.assets.items.itemlist import *

class TestItem(Test):
    def test_item(self):

        self.add_all_items()

        self.use_item(apple)
        self.use_item(poisonedapple)

        self.create_summary()
        print(self.summary)

    def test_equipment(self):

        self.add_all_items()

        leatherarmor.equip()
        sword.equip(0)
        shield.equip(1)

        self.create_summary()
        print(self.summary)
        print('')

        leatherarmor.unequip()
        sword.unequip(0)
        shield.unequip(1)

        self.create_summary()
        print(self.summary)
    
    def test_list_all_items(self):
        items = {
            'Consumables' : self.list_items('Consumables'),
            'Keyitems' : self.list_items('Keyitems'),
            'Weapons' : self.list_items('Weapons'),
            'Armor' : self.list_items('Armor'),
            'Talisman' : self.list_items('Talisman'),
            'Equipped' : self.list_equipment()
        }
        print(items)
from unittest import TestCase
from app.src.assets.player.player import Player as P
from app.src.assets.items.consumables import Consumables
from app.src.assets.equippables.basic.equipable import Equipable
from test.setup import testplayer

class Itemtest(TestCase):
    def test_items(self):
        testplayer()
        testitem= P.player.get('Items')
        for type in testitem:
            itemlist= []
            for item in testitem[type]:
                itemlist.append(item)
            for that in itemlist:
                self.item_cycle(that)
        P.update_player()
        print(P.player)

    def item_cycle(self,item):
        self.print_items(item)
        if isinstance(item, Consumables):
            P.use_item(item)
        elif isinstance(item, Equipable):
            P.equip(item)
        self.print_items(item)

    @staticmethod
    def print_items(item):
        if hasattr(item, 'affected'):
            attributes= P.return_attributes()
            statistics= P.return_statistics()
            if item.affected in attributes:
                print(attributes.get(item.affected))
            elif item.affected in statistics:
                print(statistics.get(item.affected))
        print(f'{P.return_itemnames().get(item.type)}\n')
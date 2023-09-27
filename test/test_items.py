from unittest import TestCase
from app.src.assets.player.player import Player
from app.src.assets.items.types.consumables import Consumables
from test.setup import testplayer, testitems

class Itemtest(TestCase):
    def test_items(self):
        testplayer()
        testitem=testitems()
        for item in testitem:
            self.item_cycle(item=item)

    def item_cycle(self,item):
        item.add()
        self.print_items(item)
        if isinstance(item,Consumables):
            Player.use_item(item=item)
        else: item.remove()
        self.print_items(item)

    @staticmethod
    def print_items(item):
        if hasattr(item,'affected'):
            attributes=Player.return_attributes()
            statistics=Player.return_statistics()
            if item.affected in attributes:
                print(attributes.get(item.affected))
            elif item.affected in statistics:
                print(statistics.get(item.affected))
        print(f'{Player.return_itemnames().get(item.type)}\n')
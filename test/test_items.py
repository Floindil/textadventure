from unittest import TestCase
from app.src.assets.player.player import Player
from app.src.assets.items.types.consumables import Consumables
from test.setup import testplayer, testitems

class Itemtest(TestCase):
    def test_items(self):
        testplayer()
        testitem= Player.player.get('Items')
        for type in testitem:
            itemlist= []
            for item in testitem[type]:
                itemlist.append(item)
            for that in itemlist:
                self.item_cycle(that)
        Player.update_player()
        print(Player.player)

    def item_cycle(self,item):
        self.print_items(item)
        if isinstance(item,Consumables):
            Player.use_item(item)
        else: Player.remove_item(item)
        self.print_items(item)

    @staticmethod
    def print_items(item):
        if hasattr(item, 'affected'):
            attributes= Player.return_attributes()
            statistics= Player.return_statistics()
            if item.affected in attributes:
                print(attributes.get(item.affected))
            elif item.affected in statistics:
                print(statistics.get(item.affected))
        print(f'{Player.return_itemnames().get(item.type)}\n')
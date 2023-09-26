from unittest import TestCase
from app.src.assets.player.player import Player
from test.setup import testplayer, testitems

class Itemtest(TestCase):
    def test_items(self):
        testplayer()
        testitem=testitems()
        for item in testitem:
            self.item_cycle(item=item)

    @staticmethod
    def item_cycle(item):
        item.add()
        print(Player.return_itemnames().get(item.type))
        item.remove()
        print(Player.return_itemnames().get(item.type))


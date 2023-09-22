from unittest import TestCase
from app.src.assets.player.player import Player
from test.setup import testplayer

class Playertest(TestCase):
    def test_player(self):
        testplayer()
        print(Player.return_player())
        
        
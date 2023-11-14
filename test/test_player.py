from unittest import TestCase
from app.src.assets.player.player import Player
from test.setup import testplayer

class Playertest(TestCase):
    def test_player(self):
        testplayer()
        for part in Player.player:
            '''prints all the container names'''
            print(part)
            p = Player.player.get(part)
            if isinstance(p, dict):
                '''prints first content layer if its a dict'''
                for object in p:
                    if isinstance(p.get(object), list):
                        print(f'    {object}:')
                        for element in p.get(object):
                            print(f'        {element}')
                    else:
                        print(f'    {object}: {p.get(object)}')
            elif isinstance(p, tuple):
                '''prints first content layer if its a tuple (Equipment)'''
                for this in p:
                    i = p.index(this)
                    for that in p[i]:
                        print(f'    {that}: {p[i].get(that)}')
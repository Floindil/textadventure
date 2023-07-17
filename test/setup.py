from app.src.assets.player import player
from app.src.assets.data.datahandler import Datahandler

def set_testplayer():
    player.set_info('The Tester', 'Undefined', 'Robot')
    player.set_attribute('Health', 7)
    player.set_attribute('Stamina', 3)
    player.set_attribute('Light', 2)
    player.set_attribute('Dark', 6)
    player.set_attributebonus('Health', 1)
    player.set_attributebonus('Stamina', -1)
    player.set_attributebonus('Light', 2)
    player.set_attributebonus('Dark', -3)

testdata = Datahandler()
from app.src.assets.player import player
from app.src.assets.items.itemlist import itemlist

def set_testplayer():
    player.set_info('The Tester', 'Undefined', 'Robot')
    player.change_attribute('Health', 2)
    player.change_attribute('Stamina', -2)
    player.change_attribute('Light', -2)
    player.change_attribute('Dark', 2)
    for object in itemlist:
        object.add()
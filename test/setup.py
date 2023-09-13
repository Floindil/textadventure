from methods import Test
from app.src.assets.player import player
from app.src.assets.items.itemlist import sword

t = Test()

def set_testplayer():
    player.set_state()
    player.set_info('The Tester', 'Undefined', 'Robot')
    player.set_all_attributes([4,7,3,8,10,9,4])
    player.set_attribute('Health', 1)
    player.set_all_attributes([1,1,1,-1,1,-1,-1], 1)
    player.set_attribute('Health', 2, 1)
    player.calc_all_values()
    t.clear_inventory()
    t.add_all_items()
    sword.equip()
    return player
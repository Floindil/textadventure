from app.src.assets.player.player import Player
from app.src.assets.names_values import character as c, items as i, equipment as e, attributes as a

def testplayer():
    test_character={
        c[0]:'Arbituarios',
        c[1]:'Robot',
        c[2]:'undefined'
    }
    Player.get_character(test_character)
    test_items={
        i[0]:['Drugs'],
        i[1]:['Bubble'],
        i[2]:['Horse'],
        i[3]:['Stapler'],
        i[4]:['Mouse']
    }
    Player.get_items(test_items)
    test_equipment={
        e[0]:'Starfish',
        e[1]:'Sponge',
        e[2]:'Coin',
        e[3]:'Dragon'
    }
    Player.get_equipment(test_equipment)
    test_attributes={
        a[0]:3,
        a[1]:4,
        a[2]:5,
        a[3]:6,
        a[4]:7,
        a[5]:8,
        a[6]:2
    }
    Player.get_attributes(test_attributes)
    Player.update_statistics()
    Player.recover_full()
    Player.update_value(0,-25)
    Player.update_value(1,-15)
    Player.update_value(2,-5)
    Player.update_player()
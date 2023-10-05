from app.src.assets.player.player import Player
from app.src.assets.items.types.keyitems import Keyitems as K
from app.src.assets.items.types.consumables import Consumables as C
from app.src.assets.equippables.sword import Sword as S
from app.src.assets.names_values import character as c, items as i, equipment as e, attributes as a, statistics as s

def testplayer():
    test_character= {
        c[0]: 'Arbituarios',
        c[1]: 'Robot',
        c[2]: 'undefined'
    }
    Player.get_character(test_character)

    add_testitems()
    '''test_items= {
        i[0]: ['Drugs'],
        i[1]: ['Bubble'],
        i[2]: ['Horse'],
        i[3]: ['Stapler'],
        i[4]: ['Mouse']
    }
    Player.get_items(test_items)
    test_equipment= {
        e[0]: 'Starfish',
        e[1]: 'Sponge',
        e[2]: 'Coin',
        e[3]: 'Dragon'
    }
    Player.get_equipment(test_equipment)'''
    test_attributes= {
        a[0]: 10,
        a[1]: 4,
        a[2]: 5,
        a[3]: 6,
        a[4]: 7,
        a[5]: 8,
        a[6]: 2
    }
    Player.get_attributes(test_attributes)

    Player.update_statistics()
    Player.recover_full()

    set_statistic()

    set_resources()

    Player.update_player()

def testitems():
    key= K(name= 'Testkey')
    apple= C(name= 'Apple', effect= [(s[0], 10)])
    drugs= C(name= 'Drugs', effect= [(a[1], -2)])
    raw_fish= C(name= 'Raw Fisch', effect= [(s[2], -15), (a[0], -2)])
    testsword= S('Swordus Longus', [0, 4, 2, 2, 9])
    testsword2= S('Swordus Biggus', [0, 8, 2, 2, 9], [0, 10, 0, 0, 0, 0, 0])
    return [key, apple, drugs, raw_fish, testsword, testsword2]

def add_testitems():
    items= testitems()
    for item in items:
        Player.add_item(item)

def set_statistic():
    Player.update_statvalue(s[0], -50)
    Player.update_statvalue(s[1], -15)
    Player.update_statvalue(s[2], -5)

def set_resources():
    Player.update_currency(10)
    Player.update_exp(400)
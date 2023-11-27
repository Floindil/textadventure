from app.src.assets.player.player import Player
from app.src.assets.items.others.keyitems import Keyitems as K
from app.src.assets.items.others.consumables import Consumables as C
from app.src.assets.items.others.materials import Materials as M
from app.src.assets.items.equippables.armor import Armor as A
from app.src.assets.items.equippables.sword import Sword as SW
from app.src.assets.items.equippables.greatsword import Greatsword as GS
from app.src.assets.items.equippables.shield import Shield as SH
from app.src.assets.items.equippables.talisman import Talisman as T
from app.src.assets.names_values import character as c, attributes as a, statistics as s

def testplayer():
    test_character= {
        c[0]: 'Arbituarios',
        c[1]: 'Robot',
        c[2]: 'undefined'
    }
    Player.get_character(test_character)

    key= K(name= 'Testkey')
    apple= C.apple()
    drugs= C.drugs()
    ink= M(name= 'Ink')
    raw_fish= C(name= 'Raw Fisch', effect= [(s[2], -15), (a[0], -2)])
    sword= SW.swordusLongus()
    shield= SH.i_shield()
    sword2= SW.swordusBiggus()
    greatsword= GS.swordusBiggustest()
    health_talisman = T.h_talisman()
    stamina_talisman = T.s_talisman()
    leather_armor = A.l_armor()

    add_testitems([key, drugs, drugs, raw_fish, sword, greatsword, sword, shield, sword2, ink, health_talisman, stamina_talisman, leather_armor])
    Player.add_item(apple, 5)

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

def add_testitems(items):
    for item in items:
        Player.add_item(item)

def set_statistic():
    Player.update_statvalue(s[0], -50)
    Player.update_statvalue(s[1], -15)
    Player.update_statvalue(s[2], -5)

def set_resources():
    Player.update_currency(10)
    Player.update_exp(400)

def print_player():
    for part in Player.player:
        '''prints all the container names'''
        print(part)
        p = Player.player.get(part)
        if isinstance(p, dict):
            '''prints first content layer if its a dict'''
            for object in p:
                o = p.get(object)
                if isinstance(o, list):
                    print(f'    {object}:')
                    for element in o:
                        print(f'        {element.name}')
                else:
                    print(f'    {object}: {o}')
        elif isinstance(p, tuple):
            '''prints first content layer if its a tuple (Equipment)'''
            for this in p:
                i = p.index(this)
                for that in p[i]:
                    t = p[i].get(that)
                    if isinstance(t, int) or not t or isinstance(t, tuple):
                        print(f'    {that}: {t}')
                    else: print(f'    {that}: {t.name}')
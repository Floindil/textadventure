from app.src.assets.player.player import Player
from app.src.assets.player.sources.naming import character as c, items as i, equipment as e

def testplayer():
    character={
        c[0]:'Arbituarios',
        c[1]:'Robot',
        c[2]:'undefined'
    }
    Player.get_character(character)
    items={
        i[0]:['Drugs'],
        i[1]:['Bubble'],
        i[2]:['Horse'],
        i[3]:['Stapler'],
        i[4]:['Mouse']
    }
    Player.get_items(items)
    equipment={
        e[0]:'Starfish',
        e[1]:'Sponge',
        e[2]:'Coin',
        e[3]:'Dragon'
    }
    Player.get_equipment(equipment)
    Player.create_player()
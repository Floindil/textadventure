from unittest import TestCase
from assets.player import player
from assets.items import itemtypes as i

class Itemtest(TestCase):
    def test_items(self):
        player.info['Name'] = 'Franzel'

        poisonedapple = i.Consumable('Poisoned Apple', 'An Apple, poised by the Old Witch', -2, 'Health')
        apple = i.Consumable('Apple', 'An Apple, gathered from a Appletree', 2, 'Health')

        sword = i.Weapon('Sword', 'A simple Sword', 3, None)
        leatherarmor = i.Armor('Leather Armor', 'A simple Armor made of Leather', 7, None)
        shield = i.Weapon('Shield', 'A simple Shield', 5, None)
        greatsword = i.Weapon('Greatsword', 'A simple Greatsword', 5, None)

        apple.add()
        sword.add()
        leatherarmor.add()
        shield.add()
        greatsword.add()
        poisonedapple.add()

        player.create_summary()
        print(player.summary)

        leatherarmor.equip()
        sword.equip(0)
        shield.equip(1)
        poisonedapple.use()

        print(f'Health: {player.attributes["Health"]}')

        apple.use()

        print(f'Health: {player.attributes["Health"]}')

        player.create_summary()
        print(player.summary)
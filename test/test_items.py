from unittest import TestCase
from app.src.assets.player.player import Player as P
from app.src.assets.items.others.consumables import Consumables
from app.src.assets.items.equippables.basic.equipable import Equipable
from test.setup import testplayer, i
from app.src.assets.names_values import player as p

class Itemtest(TestCase):
    def test_all(self):
        testplayer()
        print(P.player)
        testitem= P.player.get(p[1])
        for type in testitem:
            itemlist= []
            for item in testitem[type]:
                itemlist.append(item)
            for that in itemlist:
                self.item_cycle(that)
                print('\n')
        P.update_player()
        print(P.player)

    def test_consumables(self):
        testplayer()
        testitems= P.player.get(p[1])
        consumables= testitems.get(i[0])
        for item in consumables:
            self.item_cycle(item)
            print('\n')

    def test_equipment(self):
        testplayer()
        testitems= P.player.get(p[1])
        armor= testitems.get(i[2])
        weapon= testitems.get(i[1])
        talisman= testitems.get(i[3])
        itemlist = armor + weapon + talisman
        for item in itemlist:
            self.item_cycle(item)

######## Not actual tests:

    def item_cycle(self,item):
        print(f"---test item {item.name}---\n")
        self.print_items(item)
        if isinstance(item, Consumables):
            P.use_item(item)
            print(f"used item {item.name}")
        elif isinstance(item, Equipable):
            self.print_slots(item)
            equip = P.equip(item)
            if equip: print("equip success")
            else: print("requirements not met")
            self.print_slots(item)
        self.print_items(item)

    @staticmethod
    def print_items(item):
        if hasattr(item, 'effect'):
            attributes= P.return_attributes()
            statistics= P.return_statistics()
            for affected in item.effect:
                name = affected[0]
                value = affected[1]
                if name in attributes:
                    print(f'current {name}: {attributes.get(name)} value = {value}')
                elif name in statistics:
                    print(f'current {name}/max {name}: {statistics.get(name)} value = {value}')
        print(f'{item.type}: {P.return_itemnames().get(item.type)}')

    @staticmethod
    def print_slots(item):
        for slot in item.slots:
            if P.player.get(p[2]).get(slot):
                name = P.player.get(p[2]).get(slot).name
            else: name = None
            print(f'{slot}: {name}')
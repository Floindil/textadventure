from unittest import TestCase
from app.src.assets.player import player
from app.src.assets.items.itemlist import itemlist

class Test(TestCase):
    def use_item(self, item):
        print(f'use item {item.name} at {player.attributes["Health"]} health')
        item.use()
        print(f'new health: {player.attributes["Health"]}')

    def add_all_items(self):
        for object in itemlist:
            object.add()

    def clear_inventory(self):
        for type in player.itemtypes:
            player.items[type] = []
        for slot in player.slots:
            player.equipment[slot] = None

    def list_info(self, type):
        infos = ''
        for info in type:
            infos += f'{info}: {type[info]}    '
        return infos
    
    def list_items(self, type):
        list = []
        for item in player.items[type]:
            if item != None:
                list.append(item.name)
        return list
    
    def list_equipment(self):
        list = []
        for item in player.equipment:
            if player.equipment[item] != None:
                list.append(f'{item}: {player.equipment[item].name}')
            else:
                list.append(f'{item}: {player.equipment[item]}')
        return list

    def create_summary(self):        
        info = self.list_info(player.info)
        state = self.list_info(player.state)
        attributes = self.list_info(player.attributes)
        attributbonuses = self.list_info(player.attributbonuses)
        keyitems = self.list_items('Keyitems')
        consumables = self.list_items('Consumables')
        weapons = self.list_items('Weapons')
        armors = self.list_items('Armor')
        talismans = self.list_items('Talisman')
        equips = self.list_equipment()

        self.summary = f'''    {info}
    {state}
    {attributes}
    {attributbonuses}
    Keyitems: {keyitems}
    Consumables: {consumables}
    Weapons: {weapons}
    Armors: {armors}
    Talismans: {talismans}
    Equipment: {equips}'''
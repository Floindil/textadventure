from unittest import TestCase
from app.structure.assets.player import player

class Test(TestCase):
    def use_item(self, item):
        print(f'use item {item.name} at {player.attributes["Health"]} health')
        item.use()
        print(f'new health: {player.attributes["Health"]}')

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
        for item in player.items['Equipped']:
            if player.items['Equipped'][item] != None:
                list.append(f'{item}: {player.items["Equipped"][item].name}')
            else:
                list.append(f'{item}: {player.items["Equipped"][item]}')
        return list

    def create_summary(self):        
        info = self.list_info(player.info)
        attributes = self.list_info(player.attributes)
        attributbonuses = self.list_info(player.attributbonuses)
        keyitems = self.list_items('Keyitems')
        consumables = self.list_items('Consumables')
        weapons = self.list_items('Weapons')
        armors = self.list_items('Armor')
        talismans = self.list_items('Talisman')
        equips = self.list_equipment()

        self.summary = f'''    {info}
    {attributes}
    {attributbonuses}
    Keyitems: {keyitems}
    Consumables: {consumables}
    Weapons: {weapons}
    Armors: {armors}
    Talismans: {talismans}
    Equipped: {equips}'''
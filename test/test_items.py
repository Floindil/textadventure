from methods import Test
from assets.player import player
from assets.items import itemlist as il

class Itemtest(Test):
    def test_items(self):
        player.info['Name'] = 'Franzel'

        il.sword.add()
        il.leatherarmor.add()
        il.shield.add()
        il.apple.add()
        il.greatsword.add()
        il.poisonedapple.add()
        il.healthtalisman.add()
        il.testkey.add()

        self.use_item(il.apple)
        self.use_item(il.poisonedapple)

        self.create_summary()
        print(self.summary)

    def test_equipment(self):
        il.sword.add()
        il.leatherarmor.add()
        il.shield.add()

        il.leatherarmor.equip()
        il.sword.equip(0)
        il.shield.equip(1)

        self.create_summary()
        print(self.summary)

    ######################## METHODS FOR TESTING ########################

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
import json, os
from ..player import player

# used paths:
datapath = 'app/src/assets/data/savefiles/'

class Datahandler:
    def __init__(self) -> None:
        pass

    def list_items(self, type):
        list = []
        for item in player.items[type]:
            if item != None:
                list.append(item.name)
        return list
    
    def list_equipment(self):
        dict = {}
        equipment = player.items['Equipment']
        for item in equipment:
            equipped = equipment[item]
            if equipped != None:
                dict[item] = equipped.name
            else:
                dict[item] = equipped
        return dict

    def list_all_items(self):
        items = {
            'Consumables' : self.list_items('Consumables'),
            'Keyitems' : self.list_items('Keyitems'),
            'Weapons' : self.list_items('Weapons'),
            'Armor' : self.list_items('Armor'),
            'Talisman' : self.list_items('Talisman'),
            'Equipment' : self.list_equipment()
        }
        return items

    def save(self):
        items = self.list_all_items()
        savepath = f'{datapath}{player.info["Name"]}.json'
        with open(savepath, 'w') as f:
            data = {
                'Info' : player.info,
                'Languages' : player.languages,
                'Attributes' : player.attributes,
                'Attributbonuses' : player.attributbonuses,
                'Items' : items
            }
            json.dump(data, f, indent = 4)

    def load_itemtype(self, type, data):
        from ..items.itemlist import itemlist
        list = []
        for item in itemlist:
            if item.name in data['Items'][type]:
                list.append(item)
        player.items[type] = list

    def load_equipment(self, slot, data):
        loaded = data['Items']['Equipment'][slot]
        if loaded == None:
            player.items['Equipment'][slot] = None
        else:
            from ..items.itemlist import itemlist
            for item in itemlist:
                if item.name in loaded:
                    player.items['Equipment'][slot] = item

    def load_items(self, data):
        for type in player.itemtypes:
            self.load_itemtype(type, data)
        for slot in player.slots:
            self.load_equipment(slot, data)

    def load(self, name):
        with open(f'{datapath}{name}.json', 'r') as f:
            data = json.load(f)
            player.info = data['Info']
            player.languages = data['Languages']
            player.attributes = data['Attributes']
            player.attributbonuses = data['Attributbonuses']
            self.load_items(data)

    def list_savefiles(self):
        savefiles = []
        file_list = os.listdir(datapath)
        for file in file_list:
            if file.endswith('.json') == True:
                to_append = file.replace('.json', '')
                savefiles.append(to_append)
        return savefiles

datahandler = Datahandler()

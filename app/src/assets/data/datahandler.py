import json, os
from ..player import player

# used paths:
datapath = 'app/src/assets/data/savefiles/'

class Datahandler:
    def __init__(self) -> None:
        pass

    def set_dir(self):
        dir_name = player.info.get('Name')
        dir = f'{datapath}{dir_name}/'
        return dir

    def list_items(self, type):
        list = []
        for item in player.items[type]:
            if item != None:
                list.append(item.name)
        return list
    
    def list_equipment(self):
        dict = {}
        for item in player.equipment:
            equipped = player.equipment[item]
            if equipped != None:
                dict[item] = equipped.name
            else:
                dict[item] = equipped
        return dict

    def list_all_items(self):
        items = {
            'Consumables' : self.list_items('Consumables'),
            'Keyitems' : self.list_items('Keyitems'),
            'Armor' : self.list_items('Armor'),
            'Weapons' : self.list_items('Weapons'),
            'Talisman' : self.list_items('Talisman'),
        }
        return items

    def save(self):
        items = self.list_all_items()
        dir = self.set_dir()
        if not os.path.exists(dir):
            os.mkdir(dir)
        savepath = f'{dir}player.json'
        with open(savepath, 'w') as f:
            data = {
                'Info' : player.info,
                'State' : player.state,
                'Attributes' : player.attributes,
                'Attributbonuses' : player.attributbonuses,
                'Items' : items,
                'Equipment' : self.list_equipment()
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
        loaded = data['Equipment'][slot]
        if loaded == None:
            player.equipment[slot] = None
        else:
            from ..items.itemlist import itemlist
            for item in itemlist:
                if item.name in loaded:
                    player.equipment[slot] = item

    def load_items(self, data: dict):
        for type in player.itemtypes:
            self.load_itemtype(type, data)
        for slot in player.slots:
            self.load_equipment(slot, data)

    def load(self, name: str):
        with open(f'{datapath}{name}/player.json', 'r') as f:
            data = json.load(f)
            player.info = data.get('Info')
            player.state = data.get('State')
            player.attributes = data.get('Attributes')
            player.attributbonuses = data.get('Attributbonuses')
            self.load_items(data)

    def list_savefiles(self):
        savefiles = []
        savefiles = os.listdir(datapath)
        return savefiles
    
    def update_room(self, room):
        location = room.enter()
        dir = self.set_dir()
        room_dir = f'{dir}rooms.json'
        dict = {
                'location': location,
                room.name: {
                    'discovered': True,
                    'displayname': room.name
                    }
                }
        if not os.path.exists(room_dir):
            data = dict
        else:
            data = self.load_roomstate(room_dir)
            data.update(dict)
        self.save_roomstate(data, room_dir)
        
    def save_roomstate(self, data: dict, dir: str):
        with open(dir, 'w') as f:
            json.dump(data, f, indent=2)

    def load_roomstate(self, dir: str):
        with open(dir, 'r') as f:
            data = json.load(f)
        return data

datahandler = Datahandler()

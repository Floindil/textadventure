import json

class Player:
    def __init__(self):
        self.info = {
            'Name' : '',
            'Race' : '',
            'Sex' : '',
            'Languages' : []
        }
        self.attributes = {
            'Health' : 5,
            'Stamina' : 5,
            'Mana' : 5,
            'Strenght' : 5,
            'Dexterity' : 5,
            'Light' : 5,
            'Dark' : 5
        }
        self.attributbonuses = {
            'Health' : 0,
            'Stamina' : 0,
            'Mana' : 0,
            'Strenght' : 0,
            'Dexterity' : 0,
            'Light' : 0,
            'Dark' : 0
        }
        self.items = {
            'Consumables' : [],
            'Keyitems' : [],
            'Weapons' : [],
            'Armor' : [],
            'Talisman' : [],
            'Equipped' : {
                'Armor' : None,
                'Right Hand': None,
                'Left Hand': None,
                'Talisman': None
            }
        }
        self.itemtypes = ['Consumables', 'Keyitems', 'Weapons', 'Armor', 'Talisman']
        self.slots = ['Armor', 'Right Hand', 'Left Hand', 'Talisman']
        self.skills = []
        self.damage = 0

    def add_item(self, item : str, type : str):
        self.items[type].append(item)

    def remove_item(self, item :str, type : str):
        self.items[type].remove(item)
    
    def change_attribute(self, attribute : str, value : int):
        self.attributes[attribute] += value

    def equip(self, item : str, type : str, slot : str):
        if self.items['Equipped'][slot] != None:
            self.add_item(self.items['Equipped'][slot], type)
        self.remove_item(item, type)
        self.items['Equipped'][slot] = item

    def unequip(self, type :str, slot):
        self.add_item(self.items['Equipped'][slot], type)
        self.items['Equipped'][slot] = None

    def change_attributebonus(self, attribute : str, value : int):
        self.attributbonuses[attribute] += value

    def list_items(self, type):
        list = []
        for item in player.items[type]:
            if item != None:
                list.append(item.name)
        return list
    
    def list_equipment(self):
        dict = {}
        for item in player.items['Equipped']:
            if player.items['Equipped'][item] != None:
                dict[item] = player.items["Equipped"][item].name
            else:
                dict[item] = player.items["Equipped"][item]
        return dict

    def list_all_items(self):
        items = {
            'Consumables' : self.list_items('Consumables'),
            'Keyitems' : self.list_items('Keyitems'),
            'Weapons' : self.list_items('Weapons'),
            'Armor' : self.list_items('Armor'),
            'Talisman' : self.list_items('Talisman'),
            'Equipped' : self.list_equipment()
        }
        return items

    def save(self):
        items = self.list_all_items()
        with open(f'app/src/data/{self.info["Name"]}.json', 'w') as f:
            player = {
                'Info' : self.info,
                'Attributes' : self.attributes,
                'Attributbonuses' : self.attributbonuses,
                'Items' : items
            }
            json.dump(player, f, indent = 4)

    def set_info(self, name: str, sex: str, race: str):
        player.info['Name'] = name
        player.info['Sex'] = sex
        player.info['Race'] = race
        player.info['Languages'].append(race)

    def load_itemtype(self, type, data):
        from .items.itemlist import itemlist
        for item in itemlist:
            if item.name in data['Items'][type]:
                self.items[type].append(item)

    def load_equipment(self, slot, data):
        if data['Items']['Equipped'][slot] == None:
            self.items['Equipped'][slot] = None
        else:
            from .items.itemlist import itemlist
            for item in itemlist:
                if item.name in data['Items']['Equipped'][slot]:
                    self.items['Equipped'][slot] = item

    def load_items(self, data):
        for type in self.itemtypes:
            self.load_itemtype(type, data)
        for slot in self.slots:
            self.load_equipment(slot, data)

    def load(self, name):
        with open(f'app/src/data/{name}.json', 'r') as f:
            data = json.load(f)
            self.info = data['Info']
            self.attributes = data['Attributes']
            self.attributbonuses = data['Attributbonuses']
            self.load_items(data)

    def create_attributestring(self):
        labelcontent = ''
        count = 0
        for attribute in self.attributes:
            labelcontent += f'{attribute}:    '
            count += 1
            if count < len(self.attributes):
                labelcontent += '\n'
        return labelcontent

    def create_attributevaluestring(self):
        labelcontent = ''
        count = 0
        for attribute in self.attributes:
            labelcontent += str(self.attributes[attribute])
            count += 1
            if count < len(self.attributes):
                labelcontent += '\n'
        return labelcontent
    
    def create_attributebonuesesstring(self):
        labelcontent = ''
        count = 0
        for attribute in self.attributbonuses:
            labelcontent += attribute
            count += 1
            if count < len(self.attributbonuses):
                labelcontent += '\n'
        return labelcontent
    
    def create_attributebonuesesvaluestring(self):
        labelcontent = ''
        count = 0
        for attribute in self.attributbonuses:
            labelcontent += str(self.attributbonuses[attribute])
            count += 1
            if count < len(self.attributbonuses):
                labelcontent += '\n'
        return labelcontent
        
player = Player()
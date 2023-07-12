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
        self.damage = 0

    def add(self, item : str, type : str):
        self.items[type].append(item)

    def remove(self, item :str, type : str):
        self.items[type].remove(item)
    
    def change_attribute(self, attribute : str, value : int):
        self.attributes[attribute] += value

    def equip(self, item : str, type : str, slot : str):
        if self.items['Equipped'][slot] != None:
            self.add(self.items['Equipped'][slot], type)
        self.remove(item, type)
        self.items['Equipped'][slot] = item

    def unequip(self, type :str, slot):
        self.add(self.items['Equipped'][slot], type)
        self.items['Equipped'][slot] = None

    def change_attributebonus(self, attribute : str, value : int):
        self.attributbonuses[attribute] += value

    def save(self, file):
        with open(f'app/data/{file}.json', 'w') as f:
            player = {
                'Info' : self.info,
                'Attributes' : self.attributes,
                'Attributbonuses' : self.attributbonuses,
                'Items' : self.items
            }
            json.dump(player, f, indent = 4)

    def load(self, file):
        with open(f'{file}.json', 'r') as f:
            data = json.load(f)
            self.info = data['info']
            self.attributes = data['Attributes']
            self.attributbonuses = data['Attributbonuses']
            self.items = data['Items']
        
player = Player()
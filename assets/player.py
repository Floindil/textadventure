import json

class Player:
    def __init__(self, name, race, sex):
        self.name = name
        self.race = race
        self.sex = sex
        self.languages = [race]
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
            'Health' : 5,
            'Stamina' : 5,
            'Mana' : 5,
            'Strenght' : 5,
            'Dexterity' : 5,
            'Light' : 5,
            'Dark' : 5
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
        with open(f'{file}.json', 'w') as f:
            player = {
                'General' : {
                    'Name' : self.name,
                    'Race' : self.race,
                    'Sex' : self.sex
                },
                'Attributes' : self.attributes,
                'Attributbonuses' : self.attributbonuses,
                'Items' : self.items
            }
            json.dump(player, f, indent = 4)

    def load(self, file):
        with open(f'{file}.json', 'r') as f:
            data = json.load(f)
            self.name = data['General']['Name']
            self.race = data['General']['Race']
            self.sex = data['General']['Sex']
            self.attributes = data['Attributes']
            self.attributbonuses = data['Attributbonuses']
            self.consumables = data['Items']['Consumables']
            self.keyitems = data['Items']['Keyitems']
            self.weapons = data['Items']['Weapons']
            self.armor = data['Items']['Armor']
            self.talisman = data['Items']['Talisman']
            self.equipment = data['Items']['Equipped']

    def create_summary(self):
        self.summary = f'''{self.name, self.race, self.sex}
    {self.attributes}
    {self.attributbonuses}
    {self.items['Consumables']}
    {self.items['Keyitems']}
    {self.items['Weapons']}
    {self.items['Armor']}
    {self.items['Talisman']}
    {self.items['Equipped']}'''
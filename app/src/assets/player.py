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

    def set_info(self, name: str, sex: str, race: str):
        player.info['Name'] = name
        player.info['Sex'] = sex
        player.info['Race'] = race
        player.add_language(race)

    def add_item(self, item: str, type: str):
        self.items[type].append(item)

    def add_language(self, language):
        languages = self.info['Languages']
        if language not in languages:
            languages.append(language)

    def remove_item(self, item: str, type: str):
        self.items[type].remove(item)

    def set_attribute(self, attribute: str, value: int):
        self.attributes[attribute] = value
    
    def change_attribute(self, attribute: str, value: int):
        self.attributes[attribute] += value

    def set_attributebonus(self, attribute: str, value: int):
        self.attributbonuses[attribute] = value

    def change_attributebonus(self, attribute: str, value: int):
        self.attributbonuses[attribute] += value
        
    def equip(self, item: str, type: str, slot: str):
        equipped = self.items['Equipped'][slot]
        if equipped != None:
            self.add_item(equipped, type)
        self.remove_item(item, type)
        self.items['Equipped'][slot] = item

    def unequip(self, type: str, slot: str):
        self.add_item(self.items['Equipped'][slot], type)
        self.items['Equipped'][slot] = None

    def create_string(self, dict_to_stringify: dict):
        labelcontent = ''
        count = 0
        for attribute in dict_to_stringify:
            labelcontent += f'{attribute}:    '
            count += 1
            if count < len(dict_to_stringify):
                labelcontent += '\n'
        return labelcontent

    def create_valuestring(self, dict_to_stringify):
        labelcontent = ''
        count = 0
        for attribute in dict_to_stringify:
            labelcontent += str(dict_to_stringify[attribute])
            count += 1
            if count < len(dict_to_stringify):
                labelcontent += '\n'
        return labelcontent
        
player = Player()
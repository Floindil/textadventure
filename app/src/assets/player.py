class Player:
    def __init__(self):
        self.info = {
            'Name' : '',
            'Race' : '',
            'Sex' : '',
            'Languages' : []
        }
        self.attributes = {
            'Health' : '',
            'Stamina' : '',
            'Mana' : '',
            'Strenght' : '',
            'Dexterity' : '',
            'Light' : '',
            'Dark' : ''
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
            'Equipment' : {
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

    def set_playername(self, name: str):
        player.info['Name'] = name

    def set_info(self, name: str, sex: str, race: str):
        self.set_playername(name)
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

    def set_attribute(self, attribute: str, value: int, bonuses: int = 0):
        if bonuses == 1:
            self.attributbonuses[attribute] = value
        elif bonuses == 0:    
            self.attributes[attribute] = value
    
    def change_attribute(self, attribute: str, value: int, bonuses: int = 0):
        if bonuses == 1:
            self.attributbonuses[attribute] += value
        elif bonuses == 0:    
            self.attributes[attribute] += value
    
    def set_all_attributes(self, values: list, bonuses: int = 0):
        count = 0
        for attribute in self.attributes:
            if bonuses == 1:
                self.attributbonuses[attribute] = values[count]
            elif bonuses == 0:    
                self.attributes[attribute] = values[count]
            count +=1

    def change_all_attributes(self, values: list, bonuses: int = 0):
        count = 0
        for attribute in self.attributes:
            if bonuses == 1:
                self.attributbonuses[attribute] += values[count]
            elif bonuses == 0:    
                self.attributes[attribute] += values[count]
            count +=1

    def equip(self, item: str, type: str, slot: str):
        equipped = self.items['Equipment'][slot]
        if equipped != None:
            self.add_item(equipped, type)
        self.remove_item(item, type)
        self.items['Equipment'][slot] = item

    def unequip(self, type: str, slot: str):
        self.add_item(self.items['Equipment'][slot], type)
        self.items['Equipment'][slot] = None

    def list_dict(self, dict: dict, value: int= 0):
        text = ''
        count = 0
        for key in dict:
            if type(dict[key]) != list:
                count += 1
                if value == 0:
                    text += key
                elif value ==1:
                    text += str(dict[key])
                if count < len(dict):
                    text += '\n'
        return text

    def create_string(self, bonuses: int = 0, values: int = 0):
        if bonuses == 1:
            dict_to_stringify = self.attributbonuses
        elif bonuses == 0:
            dict_to_stringify = self.attributes
        labelcontent = ''
        count = 0
        for attribute in dict_to_stringify:
            if values == 1:
                labelcontent += str(dict_to_stringify[attribute])
            elif values == 0:
                labelcontent += f'{attribute}:    '
            count += 1
            if count < len(dict_to_stringify):
                labelcontent += '\n'
        return labelcontent
        
player = Player()
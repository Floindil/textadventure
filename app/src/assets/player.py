class Player:
    def __init__(self):
        self.info = {
            'Name' : '',
            'Race' : '',
            'Sex' : ''
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
            'Armor' : [],
            'On-Hand' : [],
            'Off-Hand' : [],
            'Twohanded' : [],
            'Talisman' : []
        }
        self.equipment = {
                'Armor' : None,
                'On-Hand' : None,
                'Off-Hand': None,
                'Talisman': None
            }
        self.itemtypes = []
        for type in self.items:
            self.itemtypes.append(type)
        self.slots = []
        for slot in self.equipment:
            self.slots.append(slot)

    def set_playername(self, name: str):
        player.info['Name'] = name

    def set_state(self):
        self.state = {
            'Skills' : [],
            'Languages' : [],
            'HP FP MP' : [0,0,0],
            'Damage' : [0,0,0]
        }

    def calc_value(self, hp_fp_mp: int = 0):
        self.state['HP FP MP'][hp_fp_mp] = self.maxvalue(hp_fp_mp) - self.state['Damage'][hp_fp_mp]
        return(self.state['HP FP MP'][hp_fp_mp])

    def calc_all_values(self):
        self.calc_value(0)
        self.calc_value(1)
        self.calc_value(2)

    def calc_damage(self, damage: int, hp_fp_mp: int = 0):
        if self.calc_value(hp_fp_mp) <= damage:
            self.damage_exceeded(hp_fp_mp)
        else:
            self.state['Damage'][hp_fp_mp] += damage
            self.calc_value(hp_fp_mp)

    def calc_all_damage(self, hp_damage, ap_damage, mp_damage):
        self.calc_damage(hp_damage,0)
        self.calc_damage(ap_damage,1)
        self.calc_damage(mp_damage,2)

    def damage_exceeded(self, hp_fp_mp: int = 0):
        self.state['Damage'][hp_fp_mp] = self.maxvalue(hp_fp_mp)
        self.calc_value(hp_fp_mp)
        if hp_fp_mp == 0:
            self.death()

    def death(self):
        print('\nPlayerdeath')

    def maxvalue(self, hp_fp_mp: int = 0):
        if hp_fp_mp == 0:
            maxvalue = self.attributes['Health']*15
        elif hp_fp_mp == 1:
            maxvalue = self.attributes['Stamina']*10
        elif hp_fp_mp == 2:
            maxvalue = self.attributes['Mana']*5
        return maxvalue

    def set_info(self, name: str, sex: str, race: str):
        self.set_playername(name)
        player.info['Sex'] = sex
        player.info['Race'] = race
        player.add_language(race)

    def add_item(self, item: str, type: str):
        self.items[type].append(item)

    def add_language(self, language):
        if language not in self.state['Languages']:
            self.state['Languages'].append(language)

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
        equipped = self.equipment[slot]
        if equipped != None:
            equipped.unequip()
        self.remove_item(item, type)
        self.equipment[slot] = item

    def unequip(self, type: str, slot: str):
        self.add_item(self.equipment[slot], type)
        self.equipment[slot] = None

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
    
    def clear_inventory(self):
        for type in player.items:
            player.items[type] = []
        for slot in player.equipment:
            player.equipment[slot] = None
        
player = Player()
from .basic.datahandler import Datahandler
from ..player import player
import jsonpickle

class Itemdata(Datahandler):
    def __init__(self) -> None:
        super().__init__(filetype = 'items')

    def save_data(self, data: dict):
           return super().save_data(data)
    
    def load_data(self):
           return super().load_data()

    def dump(self):
        items = {}
        for type in player.items:
            items.update({type: []})
            for item in player.items[type]:
                items[type].append(jsonpickle.encode(item))

        equipment = {}
        for slot in player.equipment:
            item = player.equipment.get(slot)
            if item:
                string = jsonpickle.encode(item)
            else:
                string = None
            equipment.update({slot: string})

        data = {
            'Items': items,
            'Equipment': equipment
        }
        self.save_data(data)

    def get(self):
        data: dict = self.load_data()

        data_items = data.get('Items')
        items = {}
        for type in data_items:
            items.update({type: []})
            for item in data_items[type]:
                items[type].append(jsonpickle.decode(item))
        
        data_equipment = data.get('Equipment')
        equipment = {}
        for slot in data_equipment:
            item = data_equipment.get(slot)
            if item:
                string = jsonpickle.decode(item)
            else:
                string = None
            equipment.update({slot: string})

        player.items = items
        player.equipment = equipment
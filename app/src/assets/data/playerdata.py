from .basic.data import Data
from ..player import player
import jsonpickle

class Playerdata(Data):
    def __init__(self) -> None:
           super().__init__(filetype = 'player')

    def save_data(self, data: dict):
           return super().save_data(data)
    
    def load_data(self):
           return super().load_data()

    def dump(self):
            location = jsonpickle.encode(player.location)
            data = {
                'Info' : player.info,
                'State' : player.state,
                'Attributes' : player.attributes,
                'Attributbonuses' : player.attributbonuses,
                'Location': location
            }
            self.save_data(data)

    def get(self):
            data: dict = self.load_data()
            player.info = data.get('Info')
            player.state = data.get('State')
            player.attributes = data.get('Attributes')
            player.attributbonuses = data.get('Attributbonuses')
            player.location = jsonpickle.decode(data.get('Location'))
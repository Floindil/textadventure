from .data.placedata import Placedata
from .data.inventorydata import Itemdata
from .data.playerdata import Playerdata

class Datahandler:
    place = Placedata()
    player = Playerdata()
    item = Itemdata()
    data = [place, player, item]

    @classmethod
    def save(cls):
        for type in cls.data:
            type.dump()

    def load(cls):
        for type in cls.data:
            type.get()
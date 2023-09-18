from methods import Test
from setup import set_testplayer
from app.src.assets.data.playerdata import Playerdata
from app.src.assets.data.inventorydata import Itemdata
from app.src.assets.data.placedata import Placedata
from app.src.assets.places.basic.place import Place

class TestData(Test):
    def test_playerdata(self):
        testplayer = set_testplayer()
        playerdata = Playerdata()
        playerdata.dump()
        playerdata.get()
        print(testplayer.info)

    def test_itemdata(self):
        testplayer = set_testplayer()
        itemdata = Itemdata()
        itemdata.dump()
        itemdata.get()
        print(testplayer.items)
        print(testplayer.equipment)

    def test_room(self):
        testplayer = set_testplayer()
        
        testroom = Place('Testroom', ['Bed', 'Wardrobe', 'Sofa'], ['Testroom1', 'Testroom2'])
        testroom1 = Place('Testroom1', ['Bed', 'Wardrobe', 'Sofa'], ['Testroom', 'Testroom2'])
        
        self.roomtest(testroom)
        self.roomtest(testroom1, False)
        print(testplayer.location)

    def roomtest(self, room, learn_name: bool=True):
        places = Placedata()
        if learn_name:
            room.learn_name()
        room.enter()
        places.dump(room)

    def test_savefiles(self):
        datahandler = Playerdata()
        datahandler.get_newest_savefile()
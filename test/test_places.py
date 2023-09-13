from methods import Test
from setup import set_testplayer
from app.src.assets.places.basic.room import Room
from app.src.assets.data.datahandler import datahandler

class TestPlaces(Test):
    def test_room(self):
        set_testplayer()
        testroom = Room('Testroom', ['Bed', 'Wardrobe', 'Sofa'], ['Testroom1', 'Testroom2'])
        testroom1 = Room('Testroom1', ['Bed', 'Wardrobe', 'Sofa'], ['Testroom', 'Testroom2'])
        
        self.roomtest(testroom)
        self.roomtest(testroom1)

    def roomtest(self, room):
        print(f'Displayname: {room.display_name}')
        print(f'Discoverystate: {room.discoverd}')
        location = room.enter()
        print(f'Location: {location}')
        print(f'Displayname: {room.display_name}')
        print(f'Discoverystate: {room.discoverd}\n')
        datahandler.update_room(room)
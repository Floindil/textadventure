from .basic.datahandler import Datahandler

class Placedata(Datahandler):
    def __init__(self) -> None:
        super().__init__(filetype = 'places')

    def save_data(self, data: dict):
           return super().save_data(data)
    
    def load_data(self):
           return super().load_data()

    def dump(self, room):
        roomname = room.name
        roomstate = self.pickle(room)
        dict = {
            roomname: roomstate
            }
        self.save_data(dict)

    def get(self):
        data: dict = self.load_data()
        roomstates = {}
        for room in data:
            roomstate = self.unpickle(room)
            roomstates.update({roomstate.name: roomstate})
        return roomstates

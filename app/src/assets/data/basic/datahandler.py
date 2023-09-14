import json, os, jsonpickle
from ...player import player
from ....resources.configuration.settings import datapath

class Datahandler:
    def __init__(self, filetype: str) -> None:
        self.filetype = filetype
        self.dir = self.set_dir()

    def set_dir(self):
        dir_name = player.info.get('Name')
        dir = f'{datapath}{dir_name}/'
        return dir

    def list_savefiles(self):
        savefiles = os.listdir(datapath)
        return savefiles
        
    def save_data(self, data: dict):
        filetosave = f'{self.dir}{self.filetype}.json'
        if os.path.exists(filetosave):
            datatosave: dict = self.load_data()
            datatosave.update(data)
        else:
            datatosave = data
        with open(filetosave, 'w') as f:
            json.dump(datatosave, f, indent=2)

    def load_data(self):
        filetoload = f'{self.dir}{self.filetype}.json'
        with open(filetoload, 'r') as f:
            data = json.load(f)
        return data
    
    def pickle(self, object):
        string = jsonpickle.encode(object)
        return string
    
    def unpickle(self, string: str):
        object = jsonpickle.decode(string)
        return object

#datahandler = Datahandler()

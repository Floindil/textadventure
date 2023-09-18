import json, os, jsonpickle
from ...player import player
from ....resources.configuration.settings import datapath

class Data:
    def __init__(self, filetype: str) -> None:
        self.filetype = filetype
        self.dir = self.set_dir()
        self.file = f'{self.dir}{self.filetype}.json'

    def set_dir(self):
        dir_name = player.info.get('Name')
        dir = f'{datapath}{dir_name}/'
        return dir

    def list_savefiles(self):
        savefiles = os.listdir(datapath)
        return savefiles
    
    def get_newest_savefile(self):
        folders = self.list_savefiles()
        savefiles = []
        if folders != []:
            for folder in folders:
                savefile = f'{datapath}{folder}/{self.filetype}.json'
                savefiles.append(savefile)
            savefiles.sort(key=lambda x: os.path.getmtime(x), reverse = True)
            name = savefiles[0].replace(datapath,'').replace(f'/{self.filetype}.json', '')
        return name
        
    def save_data(self, data: dict):
        if os.path.exists(self.file):
            datatosave: dict = self.load_data()
            datatosave.update(data)
        else:
            datatosave = data
        with open(self.file, 'w') as f:
            json.dump(datatosave, f, indent=2)

    def load_data(self):
        with open(self.file, 'r') as f:
            data = json.load(f)
        return data
    
    def pickle(self, object):
        string = jsonpickle.encode(object)
        return string
    
    def unpickle(self, string: str):
        object = jsonpickle.decode(string)
        return object

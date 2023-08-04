from ....player import player

class Item:
    def __init__(self, name : str, description : str, value : int, attributes : list) -> None:
        self.name = name
        self.type = ''
        self.attributes = attributes
        self.value = value
        self.description = description

    def add(self):
        player.add_item(self, self.type)

    def discard(self):
        player.remove_item(self, self.type)
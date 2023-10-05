from ...player.player import Player

class Item:
    def __init__(self, name: str) -> None:
        self.name= name

    def add(self):
        Player.add_item(self)

    def remove(self):
        Player.remove_item(self)

    
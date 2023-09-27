from ....player.player import Player

class Item:
    def __init__(self) -> None:
        pass

    def add(self):
        Player.add_item(self)

    def remove(self):
        Player.remove_item(self)

    
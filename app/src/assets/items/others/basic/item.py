from ....player.player import Player

class Item:
    def __init__(self, name: str) -> None:
        self.name= name
        self.amount= 0

    def add(self, amount: int= 1):
        Player.add_item(item= self, amount= amount)

    def remove(self, amount: int= 1):
        Player.remove_item(item= self, amount= amount)

    
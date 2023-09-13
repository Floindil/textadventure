class Room:
    def __init__(
            self,
            name: str,
            furniture: list,
            adjacent: list,
            size: str = 'small'
            ) -> None:
        self.name = name
        self.size = size
        self.furniture = furniture
        self.adjacent = adjacent
        self.discoverd = False
        self.display_name = 'Unknown Place'
        self.number_adjacent = len(adjacent)

    def enter(self):
        self.discoverd = True
        self.display_name = self.name
        location = self.name
        return location
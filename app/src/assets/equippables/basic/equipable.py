class Equipable:
    def __init__(
            self,
            name: str,
            slots: list,
            values: list= [0, 1, 2, 3, 4],
            requirements: list= [0, 1, 2, 3, 4, 5, 6]
            ) -> None:
        self.name= name
        self.slots= slots
        self.values= values
        if requirements==  [0, 1, 2, 3, 4, 5, 6]: requirements= None
        self.requirements= requirements
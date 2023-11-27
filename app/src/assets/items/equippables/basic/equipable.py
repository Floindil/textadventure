class Equipable:
    def __init__(
            self,
            name: str,
            slots: list,
            values: list = [0, 1, 2, 3, 4],
            buff: list = [
                ['affected value'],
                ['value']
            ],
            requirements: list= [0, 1, 2, 3, 4, 5, 6]
            ) -> None:
        '''
        buff list: [
                [affected value1, affected value2, ...]
                [value1, value2, ...]
            ],
        '''
        self.name = name
        self.slots = slots
        if values == [0, 1, 2, 3, 4]: values = None
        self.values = values
        if buff:
            self.buff = {
                'name': name,
                'type': buff[0],
                'value': buff[1]
            }
        else: self.buff = None
        if requirements ==  [0, 1, 2, 3, 4, 5, 6]: requirements= None
        self.requirements = requirements
        self.amount = 0
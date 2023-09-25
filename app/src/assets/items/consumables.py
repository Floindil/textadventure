from ..names_values import items as i

class Consumables:
    def __init__(self,name:str,affects_stat:int,value:int) -> None:
        self.type=i[0]
        self.name=name
        self.affected_stat=affects_stat
        self.value=value

    def use(self):
        pass
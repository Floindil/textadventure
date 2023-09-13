from .basic.city import City

class City1(City):
    def __init__(self) -> None:
        super().__init__('Hedorn')

city1 = City1()
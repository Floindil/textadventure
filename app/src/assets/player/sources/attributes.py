from ...names_values import attributes as a

class Attributes:
    attributes= {
        a[0]: 0,
        a[1]: 0,
        a[2]: 0,
        a[3]: 0,
        a[4]: 0,
        a[5]: 0,
        a[6]: 0
    }

    @classmethod
    def update_attribute(cls, type: str, value: int):
        old= cls.attributes.get(type)
        new= old+ value
        if new< 1: new= 1
        cls.attributes.update({type: new})

    def update(cls, change_list: list= [0, 1, 2, 3, 4, 5, 6]):
        for value in change_list:
            if value:
                index= change_list.index(value)
                new_value= cls.attributes.get(a[index])+ value
                if new_value< 0:
                    new_value= 0
                cls.attributes.update({a[index]: new_value})
    
    @classmethod
    def get_attributes(cls, dict: dict):
        for attribute in cls.attributes:
            value= dict.get(attribute)
            cls.attributes.update({attribute: value})
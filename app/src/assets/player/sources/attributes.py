from .naming import attributes

class Attributes:
    attributes={
        attributes[0]:0,
        attributes[1]:0,
        attributes[2]:0,
        attributes[3]:0,
        attributes[4]:0,
        attributes[5]:0,
        attributes[6]:0
    }

    @classmethod
    def change(cls,change_list:list=[0,1,2,3,4,5,6]):
        for value in change_list:
            if value:
                index = change_list.index(value)
                new_value = cls.attributes.get(attributes[index]) + value
                if new_value < 0:
                    new_value = 0
                cls.attributes.update({attributes[index]:new_value})

    @classmethod
    def return_attributes(cls):
        return cls.attributes
    
    @classmethod
    def get_attributes(cls,dict:dict):
        for attribute in cls.attributes:
            value=dict.get(attribute)
            cls.attributes.update({attribute:value})
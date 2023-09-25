from ...fixed_values import items

class Inventory:
    items={
        items[0]:[],
        items[1]:[],
        items[2]:[],
        items[3]:[],
        items[4]:[]
    }
    @classmethod
    def add_item(cls, item, type:list):
        type.append(item)

    @classmethod
    def remove_item(cls, item, type:list):
        type.remove(item)
    
    @classmethod
    def get_items(cls, data:dict):
        for type in cls.items:
            items = data.get(type)
            cls.items.update({type:items})
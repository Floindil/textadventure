from ...names_values import items as i

class Inventory:
    items={
        i[0]:[],
        i[1]:[],
        i[2]:[],
        i[3]:[],
        i[4]:[]
    }
    @classmethod
    def add_item(cls, item):
        cls.items[item.type].append(item)

    @classmethod
    def remove_item(cls, item):
        cls.items[item.type].remove(item)
    
    @classmethod
    def get_items(cls, data:dict):
        for type in cls.items:
            items = data.get(type)
            cls.items.update({type:items})
from ...names_values import items as i
'''
Values imported from names_values file are only stated there to allow easy name changes late in the project
'''
class Inventory:
    items= {
        i[0]: [],
        i[1]: [],
        i[2]: [],
        i[3]: [],
        i[4]: [],
        i[5]: []
    }
    @classmethod
    def add_item(cls, item, amount: int= 1):
        item.amount += amount
        if item not in cls.items[item.type]:
            cls.items[item.type].append(item)

    @classmethod
    def remove_item(cls, item, amount: int= 1):
        item.amount -= amount
        if item.amount < 1:
            cls.items[item.type].remove(item)
    
    @classmethod
    def get_items(cls, data: dict):
        for type in cls.items:
            items= data.get(type)
            cls.items.update({type: items})
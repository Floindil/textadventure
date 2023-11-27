from ...names_values import attributes as a, statistics as s, equipment_values as ev
'''
Values imported from names_values file are only stated there to allow easy name changes late in the project
'''
class Buffs:
    buffs= {}
    values= {
        s[0]: 0,
        s[1]: 0,
        s[2]: 0,
        a[0]: 0,
        a[1]: 0,
        a[2]: 0,
        a[3]: 0,
        a[4]: 0,
        a[5]: 0,
        a[6]: 0,
        ev[0]: 0,
        ev[1]: 0,
        ev[2]: 0,
        ev[3]: 0,
        ev[4]: 0
    }
    
    @classmethod
    def update_buff(
        cls,
        buff: dict,
        remove: bool= False
        ):
        '''
        type: [type1, type2, ...]
        value: [value1, value2, ...] needs to be corresponding to type
        to remove buff, set remove = True
        '''
        name = buff.get('name')
        type = buff.get('type')
        value = buff.get('value')
        for t in type:
            i = type.index(t)
            old_value = cls.values.get(t)

            if not remove:
                cls.buffs.update({name: (type[i], value[i])})
                new_value = old_value + value[i]

            elif remove:
                new_value = old_value - value[i]

            cls.values.update({t: new_value})
        if remove: cls.buffs.pop(name)
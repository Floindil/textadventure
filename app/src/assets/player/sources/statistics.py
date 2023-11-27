from ...names_values import statistics as s, statistics_values as sv, attributes as a
from .attributes import Attributes as A
from .buffs import Buffs as B
'''
Values imported from names_values file are only stated there to allow easy name changes late in the project
'''
class Statistics:
    statistics= {
        s[0]: 0,
        s[1]: 0,
        s[2]: 0
    }
    values = {
        s[0]: 0,
        s[1]: 0,
        s[2]: 0
    }

    @staticmethod
    def calculate_statistics():
        stat0= (A.values.get(a[0]) + B.values.get(a[0]))* sv[0]
        stat1= (A.values.get(a[1]) + B.values.get(a[1]))* sv[1]
        stat2= (A.values.get(a[4]) + B.values.get(a[4]))* sv[2]
        return [stat0, stat1, stat2]
    
    @classmethod
    def update_statistics(cls):
        stats= cls.calculate_statistics()
        for stat in stats:
            i= stats.index(stat)
            stat= stats[i] + B.values.get(s[i])
            if cls.values[s[i]] > stat: cls.values[s[i]] = stat
            cls.statistics.update({s[i]: stat})

    @classmethod
    def update_value(cls, type: int, value: int):
        newvalue= cls.values.get(type)+ value
        maxvalue= cls.statistics.get(type) + B.values.get(type)
        if newvalue< 0: newvalue= 0
        elif newvalue> maxvalue: newvalue= maxvalue
        cls.values.update({type: newvalue})

    @classmethod
    def recover_value(cls, type: str):
        '''
        restore value to maximum
        see type in names_values file
        '''
        maxvalue= cls.statistics.get(type) + B.values.get(type)
        cls.values.update({type: maxvalue})

    @classmethod
    def recover_full(cls):
        cls.recover_value(s[0])
        cls.recover_value(s[1])
        cls.recover_value(s[2])
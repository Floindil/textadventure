from ...names_values import statistics as s, statistics_values as sv
from .attributes import Attributes as A, a

class Statistics:
    statistics={
        s[0]:(0,0),
        s[1]:(0,0),
        s[2]:(0,0)
    }

    @staticmethod
    def calculate_statistics():
        stat0=A.attributes.get(a[0])*sv[0]
        stat1=A.attributes.get(a[1])*sv[1]
        stat2=A.attributes.get(a[4])*sv[2]
        return [stat0,stat1,stat2]
    
    @classmethod
    def update_statistics(cls):
        stat=cls.calculate_statistics()
        cls.statistics.update(
            {
                s[0]:(cls.statistics[s[0]][0],stat[0]),
                s[1]:(cls.statistics[s[1]][0],stat[1]),
                s[2]:(cls.statistics[s[2]][0],stat[2]),
            }
        )

    @classmethod
    def update_value(cls,type:int,value:int):
        oldvalue=cls.statistics.get(s[type])[0]
        newvalue=oldvalue+value
        maxvalue=cls.statistics.get(s[type])[1]
        if newvalue<0: newvalue=0
        elif newvalue>maxvalue: newvalue=maxvalue
        cls.statistics.update({s[type]:(newvalue,maxvalue)})

    @classmethod
    def recover_value(cls,type:int):
        maxvalue=cls.statistics[s[type]][1]
        cls.statistics.update({s[type]:(maxvalue,maxvalue)})

    @classmethod
    def recover_full(cls):
        cls.recover_value(0)
        cls.recover_value(1)
        cls.recover_value(2)
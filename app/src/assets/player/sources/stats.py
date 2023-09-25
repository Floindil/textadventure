from ...names import stats
from .attributes import Attributes as A, attributes as a

class Stats:
    stats={
        stats[0]:0,
        stats[1]:0,
        stats[2]:0,
        stats[3]:0
    }

    @staticmethod
    def calculate_stats():
        stat0 = A.attributes.get(a[0])*15
        stat1 = A.attributes.get(a[1])*10
        stat2 = A.attributes.get(a[4])*10
        return [stat0,stat1,stat2]
    
    @classmethod
    def update_stats(cls):
        stat = cls.calculate_stats()
        cls.stats.update(
            {
                stats[0]:stat[0],
                stats[1]:stat[1],
                stats[2]:stat[2],
            }
        )
    
    @classmethod
    def update_armor(cls, value:int):
        armorvalue=int(cls.stats.get(stats[3]))
        newvalue=armorvalue+value
        cls.stats.update({stats[3]:newvalue})

    def return_stats(cls):
        return cls.stats
from .stat import Stat
from .utils import GET_TRUNC_NORM, STATS_DICT

class Person:
    def __init__(self, age, name):
        self.stats = {}
        self.first_name, self.last_name = name
        self.name = self.first_name + " " + self.last_name
        self.age = round(age)
        for stat in STATS_DICT.keys():
            var = STATS_DICT[stat]["RANGE"]
            peak = STATS_DICT[stat]["PEAK"]
            decay = STATS_DICT[stat]["DECAY"]
            self.stats[stat] = Stat(var, peak, decay)
    def __repr__(self):
        return """
        Name: {}
        Age: {}
        PWR: {}
        RFX: {}
        MTL: {}
        """.format(self.name, self.age, self.stats["PWR"].get_str(self.age), self.stats["RFX"].get_str(self.age), self.stats["MTL"].get_str(self.age))

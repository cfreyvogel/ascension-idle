from oracle import ORACLE
from scipy.stats import truncnorm
def GET_TRUNC_NORM(sd, low, up):
            mean = (low+up)/2
            return truncnorm((low - mean) / sd, (up - mean) / sd, loc=mean, scale=sd)

GLOBALS = {
    "MAX_AGE": 100,
    "MARRY_AGE": (13, 60)
}
STATS = {
    "PWR": {
        "RANGE": (1, 3, 18), #standard_deviation, lower bound, upper bound
        "PEAK": 25,
        "DECAY": (40, .5), # They will lose 50% of their strength by the time they hit MAX_AGE
    }, 
    "DEX": {
        "RANGE": (1, 3, 18), #standard_deviation, lower bound, upper bound
        "PEAK": 25,
        "DECAY": (40, .5), # They will lose 50% of their strength by the time they hit MAX_AGE
    }, 
    "MTL": {
        "RANGE": (1, 3, 18), #standard_deviation, lower bound, upper bound
        "PEAK": 25,
        "DECAY": (40, .5), # They will lose 50% of their strength by the time they hit MAX_AGE
    }
}

class Stat:
    """ The instantiation of a particular stat for an individual """
    def __init__(self, variance, peak_age, decay, _max=None):
        self.variance = variance
        self.peak_age = peak_age
        self.decay = decay
        self._max = round(GET_TRUNC_NORM(*variance)) if not _max else _max

    def get_current(self, age):
        if self.age <= peak:
                return (age/peak) * _max
            elif age > dec_age:
                return _max * ((1 - (age-dec_age) / (GLOBALS["MAX_AGE"] - dec_age)))
            else:
                return _max
    def __repr__(self):
        return "{}/{}".format(self.current, self.max)
    def update(self):

for i in STATS.keys():
    ORACLE.prt(i)
    ORACLE.prt(STATS[i])

class Person:
    def __init__(self, age, name):
        self.stats = {}
        self.first_name, self.last_name = name
        self.age = age
        for stat in STATS.keys:
            var = STATS[stat]["RANGE"]
            peak = STATS[stat]["PEAK"]
            decay = STATS[stat]["DECAY"]
            self.stats[stat] = Stat(var, peak, decay)

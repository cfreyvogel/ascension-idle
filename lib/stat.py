from .utils import GET_TRUNC_NORM, GLOBALS, STATS_DICT

class Stat:
    """ The instantiation of a particular stat for an individual """
    def __init__(self, variance, peak_age, decay, _max=None):
        self.variance = variance
        self.peak_age = peak_age
        self.decay_age, self.decay_rate = decay
        self._max = round(GET_TRUNC_NORM(*variance)) if not _max else _max

    def get_current(self, age):
        if age <= self.peak_age:
            return round((age/self.peak_age) * self._max)
        elif age > self.decay_age:
            return round(self._max * (((age-self.decay_age) / (GLOBALS["MAX_AGE"] - self.decay_age)) * self.decay_rate))
        else:
            return self._max
    def get_str(self,age):
        return "{}/{}".format(self.get_current(age), self._max)
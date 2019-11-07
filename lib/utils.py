from scipy.stats import truncnorm

def GET_TRUNC_NORM(sd, low, up, mean=None):
    mean = (low+up)/2 if not mean else mean
    return truncnorm((low - mean) / sd, (up - mean) / sd, loc=mean, scale=sd).rvs()

GLOBALS = {
    "MAX_AGE": 100,
    "MARRY_AGE": (13, 60)
}
STATS_DICT = {
    "PWR": {
        "RANGE": (2.958, 3, 18), #standard_deviation, lower bound, upper bound
        "PEAK": 25,
        "DECAY": (40, .5), # They will lose 50% of their strength by the time they hit MAX_AGE
    }, 
    "RFX": {
        "RANGE": (2.958, 3, 18), #standard_deviation, lower bound, upper bound
        "PEAK": 15,
        "DECAY": (40, .5), # They will lose 50% of their strength by the time they hit MAX_AGE
    }, 
    "MTL": {
        "RANGE": (2.958, 3, 18), #standard_deviation, lower bound, upper bound
        "PEAK": 25,
        "DECAY": (60, .9), # They will lose 50% of their strength by the time they hit MAX_AGE
    }
}
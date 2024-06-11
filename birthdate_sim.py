import numpy as np
import random
from collections import Counter


def draw_n_birth_dates(people):
    '''
    For a grio
    '''
    DAYS = range(1,366) 
    return [random.choice(DAYS) for _ in range(1,people+1)]

def repeat_draws(samples,people):
    return [draw_n_birth_dates(people) for i in range(samples)]


def simulate_birthdate_draws(samples,people):
     return repeat_draws(samples,people)



def tally_shared_birthdates(samples,sample_birth_dates):

    per_date_counts = np.zeros((samples,366),dtype=int)

    for sample, draw in enumerate(sample_birth_dates):
        ## Count dates frequency
        dates_frequency = Counter(draw)
        per_date_counts[sample,list(dates_frequency.keys())] = list(dates_frequency.values())
    
    return per_date_counts

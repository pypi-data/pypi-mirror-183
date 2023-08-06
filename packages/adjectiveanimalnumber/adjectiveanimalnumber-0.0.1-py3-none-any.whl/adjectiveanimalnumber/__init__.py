from adjectiveanimalnumber.animals import animals
from adjectiveanimalnumber.adjectives import adjectives

import random


def _generate_adjectives(n_adjectives):
    for _ in range(n_adjectives):
        yield random.choice(adjectives)


def generate(n_adjectives=1, sep="-", randint=True, inf=0, sup=100):
    """
    Generate random adjectives with an animal name and a random integer.
    :param n_adjectives: number of adjectives to use
    :param sep: separator for terms
    :param randint: tells if a random integer should be added
    :param inf: inferior limit for random integer
    :param sup: superior limit for random integer
    :return: random generated string
    """
    r_animal = random.choice(animals)
    r_adjectives = sep.join(_generate_adjectives(n_adjectives))
    aa = r_adjectives + sep + r_animal
    if randint:
        aa += sep + str(random.randint(inf, sup))
    return aa


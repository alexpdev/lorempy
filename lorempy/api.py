from itertools import cycle, chain
from lorempy.text import STANDARD, EXTENDED

def full_text():
    return STANDARD

def extended_text():
    return EXTENDED

def all_words():
    standard_words = STANDARD.split(" ")
    extended_words = EXTENDED.split(" ")
    iterator = chain.from_iterable(standard_words, extended_words)
    seq = cycle(iterator)
    while True:
        yield next(seq)


def words():
    standard_words = STANDARD.split(" ")
    it = cycle(standard_words)
    while True:
        yield next(it)

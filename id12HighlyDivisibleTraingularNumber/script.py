import itertools
import math


def triangle_numbers():
    return itertools.accumulate(itertools.count())


def get_factors(n):
    factors = set()
    factors.update([1])
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            factors.update([i, n // i])
    return factors


def answer():
    for number in triangle_numbers():
        if len(get_factors(number)) >= 500:
            return number


print(answer())
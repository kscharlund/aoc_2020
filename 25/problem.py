import sys
from pprint import pprint
import math


def memoize(func):
    """
    Memoization decorator for a function taking a single argument.
    """
    class Memodict(dict):
        """Memoization dictionary."""
        def __missing__(self, key):
            ret = self[key] = func(key)
            return ret
    return Memodict().__getitem__


MODULUS = 20201227

def get_e(pk):
    ee = 1
    while pow(7, ee, MODULUS) != pk:
        ee += 1
    return ee


def a(pk1, pk2):
    exps = [get_e(pk) for pk in (pk1, pk2)]
    print(*zip((pk1, pk2), exps))
    print(pow(pk2, exps[0], MODULUS))


def b():
    pass


def main():
    pk1, pk2 = [int(line.strip()) for line in sys.stdin]
    a(pk1, pk2)
    print()
    b()


if __name__ == '__main__':
    main()

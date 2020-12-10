import sys
from pprint import pprint
from math import prod


def a(adapters):
    diffs = [b - a for a, b in zip([0] + adapters, adapters + [adapters[-1]+3])]
    hist = {}
    for diff in diffs:
        hist[diff] = hist.get(diff, 0) + 1
    print(hist[1] * hist[3])


num_combs = [1, 1, 2, 4, 7]


def b(adapters):
    diffs = [b - a for a, b in zip([0] + adapters, adapters + [adapters[-1]+3])]
    runs = []
    rlen = 0
    for diff in diffs:
        if diff == 1:
            rlen += 1
        else:
            if rlen:
                runs.append(rlen)
            rlen = 0
    print(prod(num_combs[run] for run in runs))


def main():
    adapters = list(sorted(int(line.strip()) for line in sys.stdin.readlines()))
    a(adapters)
    print()
    b(adapters)


if __name__ == '__main__':
    main()

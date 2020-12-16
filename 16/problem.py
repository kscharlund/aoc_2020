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


def parse_input():
    field_ranges = {}
    line = sys.stdin.readline().strip()
    while line:
        field, ranges = line.split(': ')
        ranges = ranges.split(' or ')
        field_ranges[field] = [[int(x) for x in r.split('-')] for r in ranges]
        line = sys.stdin.readline().strip()

    line = sys.stdin.readline().strip()
    assert line == 'your ticket:'
    your_ticket = [int(x) for x in sys.stdin.readline().strip().split(',')]
    line = sys.stdin.readline().strip()

    line = sys.stdin.readline().strip()
    assert line == 'nearby tickets:'
    nearby_tickets = [[int(x) for x in l.strip().split(',')] for l in sys.stdin.readlines()]

    return field_ranges, nearby_tickets, your_ticket


def get_valid_fields(value, field_ranges):
    valid_fields = set()
    for field, ranges in field_ranges.items():
        for lo, hi in ranges:
            if lo <= value <= hi:
                valid_fields.add(field)
    return valid_fields


def a(field_ranges, nearby_tickets):
    res = 0
    for ticket in nearby_tickets:
        for value in ticket:
            if not get_valid_fields(value, field_ranges):
                res += value
    print(res)


def b(field_ranges, nearby_tickets, your_ticket):
    valid_fields = [[get_valid_fields(v, field_ranges) for v in t] for t in nearby_tickets]
    valid_fields = [vf for vf in valid_fields if all(vf)]
    valid_union = [set(field_ranges.keys()) for _ in range(len(valid_fields[0]))]
    for ticket in valid_fields:
        for ii, valid in enumerate(ticket):
            valid_union[ii] &= valid

    undecided = {ii for ii in range(len(valid_union)) if len(valid_union[ii]) > 1}
    decided = {ii for ii in range(len(valid_union)) if len(valid_union[ii]) == 1}
    while undecided:
        for ii in decided:
            for jj in undecided:
                valid_union[jj] -= valid_union[ii]
        undecided = {ii for ii in range(len(valid_union)) if len(valid_union[ii]) > 1}
        decided = {ii for ii in range(len(valid_union)) if len(valid_union[ii]) == 1}

    res = 1
    for ii, field_set in enumerate(valid_union):
        for field in field_set:
            if field.startswith('departure'):
                res *= your_ticket[ii]
    print(res)


def main():
    field_ranges, nearby_tickets, your_ticket = parse_input()
    a(field_ranges, nearby_tickets)
    print()
    b(field_ranges, nearby_tickets, your_ticket)


if __name__ == '__main__':
    main()

from collections import namedtuple

Eq = namedtuple("Eq", ("result", "values"))

with open("input.txt") as input_file:
    def parse_line(line):
        result, values = line.split(":")
        return Eq(
            result=int(result),
            values=[int(x) for x in values.split()],
        )
    lines = [parse_line(line) for line in input_file]


#### Part1 ####
import itertools
from operator import add, mul

def check_equation(eq):
    for c in itertools.product((add, mul), repeat=len(eq.values) - 1):
        res = eq.values[0]
        for op, val in zip(c, eq.values[1:]):
            res = op(res, val)
            if res > eq.result:
                break
        if res == eq.result:
            return res
    return 0

print(sum(check_equation(l) for l in lines))

#### Part2 ####
def concat(a, b):
    return b + a * 10 ** len(str(b))

def check_equation_p2(eq):
    for c in itertools.product((add, mul, concat), repeat=len(eq.values) - 1):
        res = eq.values[0]
        for op, val in zip(c, eq.values[1:]):
            res = op(res, val)
            if res > eq.result:
                break
        if res == eq.result:
            return res
    return 0

print(sum(check_equation_p2(l) for l in lines))

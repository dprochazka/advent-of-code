with open("input.txt") as input_file:
    lines = [list(map(int, line.split())) for line in input_file]

import itertools

#### Part1 ####
def is_safe(report):
    inc = report[0] <= report[1]
    for a, b in itertools.pairwise(report):
        if not 1 <= abs(a - b) <= 3:
            return False
        if (a < b) is not inc:
            return False
    return True

print(sum(map(is_safe, lines)))


#### Part2 ####
def is_safe_p2_bruteforce(report):
    return any(map(is_safe, itertools.combinations(report, len(report) - 1)))

print(sum(map(is_safe_p2_bruteforce, lines)))

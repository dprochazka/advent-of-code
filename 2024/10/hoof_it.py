from itertools import product
from functools import cache

with open("input.txt") as input_file:
    topomap = [[int(x) for x in line.rstrip()] for line in input_file]

M, N = len(topomap), len(topomap[0])

#### Part1 ####
@cache
def find_accesible_nines(i, j, expected_height):
    if i < 0 or i >= M or j < 0 or j >= N:
        return set()
    height = topomap[i][j]
    if height != expected_height:
        return set()
    if height == 9:
        return {(i, j)}
    return (
        find_accesible_nines(i - 1, j, height + 1)
        | find_accesible_nines(i + 1, j, height + 1)
        | find_accesible_nines(i, j - 1, height + 1)
        | find_accesible_nines(i, j + 1, height + 1)
    )

score = 0
for i, j in product(range(M), range(N)):
    if topomap[i][j] == 0:
        score += len(find_accesible_nines(i, j, 0))

print(score)


#### Part2 ####
@cache
def count_trails(i, j, expected_height):
    if i < 0 or i >= M or j < 0 or j >= N:
        return 0
    height = topomap[i][j]
    if height != expected_height:
        return 0
    if height == 9:
        return 1
    return (
        count_trails(i - 1, j, height + 1)
        + count_trails(i + 1, j, height + 1)
        + count_trails(i, j - 1, height + 1)
        + count_trails(i, j + 1, height + 1)
    )


score = 0
for i, j in product(range(M), range(N)):
    if topomap[i][j] == 0:
        score += count_trails(i, j, 0)

print(score)

import itertools
from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Point2D:
    x: int
    y: int

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)


antennas = defaultdict(list)  # frequency: locations

with open("input.txt") as input_file:
    for i, line in enumerate(input_file):
        for j, c in enumerate(line.rstrip()):
            if c == ".":
                continue
            antennas[c].append(Point2D(i, j))
    M, N = i + 1, j + 1


#### Part1 ####
def find_antinodes(ant1, ant2):
    delta = ant2 - ant1
    n1 = ant1 - delta
    if 0 <= n1.x < M and 0 <= n1.y < N:
        yield n1
    n2 = ant2 + delta
    if 0 <= n2.x < M and 0 <= n2.y < N:
        yield n2


antinode_map = {}

for loc in antennas.values():
    for ant1, ant2 in itertools.combinations(loc, 2):
        for point in find_antinodes(ant1, ant2):
            antinode_map[point] = True

print(len(antinode_map))


#### Part2 ####
def find_antinodes_p2(ant1, ant2):
    delta = ant2 - ant1
    n1 = ant1
    while 0 <= n1.x < M and 0 <= n1.y < N:
        yield n1
        n1 -= delta
    n2 = ant2
    while 0 <= n2.x < M and 0 <= n2.y < N:
        yield n2
        n2 += delta


antinode_map = {}

for loc in antennas.values():
    for ant1, ant2 in itertools.combinations(loc, 2):
        for point in find_antinodes_p2(ant1, ant2):
            antinode_map[point] = True

print(len(antinode_map))

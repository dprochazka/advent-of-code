import itertools
# import math

def parse_universe(lines):
    empty_horizontal = set(range(len(lines)))
    empty_vertical = set(range(len(lines[0])))
    galaxies = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                galaxies.append((i, j))
                empty_horizontal = empty_horizontal - {i}
                empty_vertical = empty_vertical - {j}
    return galaxies, empty_horizontal, empty_vertical

def measure_universe(lines):
    galaxies, eh, ev = parse_universe(lines)
    total_distance = 0
    for g1, g2 in itertools.combinations(galaxies, 2):
        vertical_distance = abs(g1[0] - g2[0]) + len(set(range(min(g1[0], g2[0]), max(g1[0], g2[0]))) & eh)
        horizontal_distance = abs(g1[1] - g2[1]) + len(set(range(min(g1[1], g2[1]), max(g1[1], g2[1]))) & ev)
        total_distance += (horizontal_distance + vertical_distance)
    return total_distance

if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(measure_universe(lines))

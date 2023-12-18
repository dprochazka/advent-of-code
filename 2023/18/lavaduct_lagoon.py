from dataclasses import dataclass
from enum import Enum
import itertools


class Direction(Enum):
    R = "R"
    L = "L"
    U = "U"
    D = "D"

    def coord(self):
        if self == Direction.R:
            return (1, 0)
        elif self == Direction.L:
            return (-1, 0)
        elif self == Direction.U:
            return (0, 1)
        elif self == Direction.D:
            return (0, -1)

    @classmethod
    def from_num(cls, num):
        return [Direction.R, Direction.D, Direction.L, Direction.U][num]


@dataclass(frozen=True)
class Instruction:
    d: Direction
    l: int

    @classmethod
    def from_string(cls, s):
        # Part One
        d, l, c = s.split()
        return cls(Direction(d), int(l))

    @classmethod
    def from_hex(cls, s):
        # Part Two
        _, h = s.strip(")").split("#")
        return cls(Direction.from_num(int(h[-1])), int(h[:-1], base=16))


def _measure_lagoon(instructions):
    path = [(0, 0)]
    corners_left = []
    corners_right = []
    for i1, i2 in itertools.pairwise([*instructions, instructions[0], instructions[1]]):
        x0, y0 = path[-1]
        dx, dy = i1.d.coord()
        x, y = x0 + i1.l * dx, y0 + i1.l * dy
        path.append((x, y))

        # TODO generalize this with coord() some day
        if i1.d == Direction.U and i2.d == Direction.L:
            corners_left.append((x - 0.5, y - 0.5))  # inner turn
            corners_right.append((x + 0.5, y + 0.5))  # outer turn
        elif i1.d == Direction.U and i2.d == Direction.R:
            corners_left.append((x - 0.5, y + 0.5))  # outer turn
            corners_right.append((x + 0.5, y - 0.5))  # inner turn
        elif i1.d == Direction.D and i2.d == Direction.R:
            corners_left.append((x + 0.5, y + 0.5))
            corners_right.append((x - 0.5, y - 0.5))
        elif i1.d == Direction.D and i2.d == Direction.L:
            corners_left.append((x + 0.5, y - 0.5))
            corners_right.append((x - 0.5, y + 0.5))
        elif i1.d == Direction.L and i2.d == Direction.U:
            corners_left.append((x - 0.5, y - 0.5))
            corners_right.append((x + 0.5, y + 0.5))
        elif i1.d == Direction.L and i2.d == Direction.D:
            corners_left.append((x + 0.5, y - 0.5))
            corners_right.append((x - 0.5, y + 0.5))
        elif i1.d == Direction.R and i2.d == Direction.D:
            corners_left.append((x + 0.5, y + 0.5))
            corners_right.append((x - 0.5, y - 0.5))
        elif i1.d == Direction.R and i2.d == Direction.U:
            corners_left.append((x - 0.5, y + 0.5))
            corners_right.append((x + 0.5, y - 0.5))

    def volume_using_trapezoids(nodes):
        volume = 0
        for (x1, y1), (x2, y2) in itertools.pairwise([*nodes, nodes[0]]):
            volume += 0.5 * (y1 + y2) * (x1 - x2)
        return abs(volume)

    v1 = volume_using_trapezoids(corners_left)
    v2 = volume_using_trapezoids(corners_right)
    # whichever of these is smaller is the inner volume only
    # the other one includes the original digger's path
    return int(max(v1, v2))


def measure_lagoon(part, lines):
    if part == 1:
        instructions = [Instruction.from_string(l) for l in lines]
    elif part == 2:
        instructions = [Instruction.from_hex(l) for l in lines]
    return _measure_lagoon(instructions)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    # print(measure_lagoon_pipemaze(lines))
    print(measure_lagoon(2, lines))

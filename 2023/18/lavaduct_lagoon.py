from dataclasses import dataclass
from enum import Enum
import matplotlib.pyplot as plt

class Direction(Enum):
    R = "R"
    L = "L"
    U = "U"
    D = "D"

    def coord(self):
        if self == Direction.R:
            return (1,0)
        elif self == Direction.L:
            return (-1, 0)
        elif self == Direction.U:
            return (0, 1)
        elif self == Direction.D:
            return (0, -1)

@dataclass(frozen=True)
class Instruction:
    d: Direction
    l: int
    c: str

    @classmethod
    def from_string(cls, s):
        d, l, c = s.split()
        return cls(Direction(d), int(l), c.strip("()"))

def parse_input(lines):
    return [Instruction.from_string(l) for l in lines]

def measure_lagoon(lines):
    instructions = parse_input(lines)
    path = [(0, 0)]
    for i in instructions:
        for _ in range(i.l):
            x0, y0 = path[-1]
            dx, dy = i.d.coord()
            path.append((x0 + dx, y0 + dy))

    x_min = min(p[0] for p in path)
    y_min = min(p[1] for p in path)
    x_max = max(p[0] for p in path)
    y_max = max(p[1] for p in path)

    path = set(path)
    inside_vol = 0
    for y in range(y_min, y_max+1):
        inside = False
        segment_start = None
        for x in range(x_min, x_max+1):
            if {(x, y), (x, y-1), (x, y+1)} <= path:
                # vertical segment
                inside = not inside
            elif {(x,y), (x-1, y), (x+1, y)} <= path:
                # horizontal segment - no change
                pass
            elif {(x,y), (x+1, y), (x, y+1)} <= path:
                # L segment
                segment_start = "L"
            elif {(x,y), (x+1, y), (x, y-1)} <= path:
                # F segment
                segment_start = "F"
            elif {(x,y), (x-1, y), (x, y+1)} <= path:
                # J segment
                if segment_start == "F":
                    inside = not inside
                segment_start = None
            elif {(x,y), (x-1, y), (x, y-1)} <= path:
                # 7 segment
                if segment_start == "L":
                    inside = not inside
                segment_start = None
            if inside and (x,y) not in path:
                inside_vol += 1
    return inside_vol + len(path)

def visualize_lagoon(lines):
    instructions = parse_input(lines)
    path = [(0, 0)]
    for i in instructions:
        for _ in range(i.l):
            x0, y0 = path[-1]
            dx, dy = i.d.coord()
            path.append((x0 + dx, y0 + dy))
    plt.plot([p[0] for p in path], [p[1] for p in path])
    plt.show()

if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(measure_lagoon(lines))

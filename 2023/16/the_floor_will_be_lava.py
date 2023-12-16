from enum import Enum
from functools import cache


class Direction(Enum):
    N = (-1, 0)
    S = (1, 0)
    W = (0, -1)
    E = (0, 1)


def count_energized(field, start):
    M = len(field)
    N = len(field[0])
    beams = [start]
    history = set(beams)

    @cache
    def is_outside(i, j, d):
        return i < 0 or i >= M or j < 0 or j >= N

    @cache
    def advance(i, j, d):
        i += d.value[0]
        j += d.value[1]
        return i, j, d

    while len(beams):
        i, j, d = beams.pop()  # fifo
        cur = field[i][j]
        if (
            cur == "."
            or (cur == "|" and d in {Direction.N, Direction.S})
            or (cur == "-" and d in {Direction.E, Direction.W})
        ):
            b = advance(i, j, d)
            if not is_outside(*b) and b not in history:
                beams.append(b)
        elif cur == "|" and d in {Direction.W, Direction.E}:
            for b in [(i, j, Direction.N), (i, j, Direction.S)]:
                if b not in history:
                    beams.append(b)
        elif cur == "-" and d in {Direction.N, Direction.S}:
            for b in [(i, j, Direction.W), (i, j, Direction.E)]:
                if b not in history:
                    beams.append(b)
        elif cur == "/":
            if d == Direction.N:
                d = Direction.E
            elif d == Direction.W:
                d = Direction.S
            elif d == Direction.S:
                d = Direction.W
            elif d == Direction.E:
                d = Direction.N
            b = advance(i, j, d)
            if not is_outside(*b) and b not in history:
                beams.append(b)
        elif cur == "\\":
            if d == Direction.N:
                d = Direction.W
            elif d == Direction.W:
                d = Direction.N
            elif d == Direction.S:
                d = Direction.E
            elif d == Direction.E:
                d = Direction.S
            b = advance(i, j, d)
            if not is_outside(*b) and b not in history:
                beams.append(b)
        history |= set(beams)

    energized = {(i, j) for i, j, _ in history}
    return len(energized)


def part_one(field):
    return count_energized(field, (0, 0, Direction.E))


def part_two(field):
    M = len(field)
    N = len(field[0])
    top = [(0, i, Direction.S) for i in range(N)]
    bottom = [(M - 1, i, Direction.N) for i in range(N)]
    left = [(i, 0, Direction.E) for i in range(M)]
    right = [(i, N - 1, Direction.W) for i in range(M)]

    return max(count_energized(field, s) for s in top + bottom + left + right)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(part_one(lines))
    print(part_two(lines))

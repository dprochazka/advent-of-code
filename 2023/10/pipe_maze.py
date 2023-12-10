from enum import Enum


class Direction(Enum):
    N = (-1, 0)
    S = (1, 0)
    W = (0, -1)
    E = (0, 1)

    def reverse(self):
        return Direction((-self.value[0], -self.value[1]))


def parse_pipe(char):
    d = {
        "|": {Direction.N, Direction.S},
        "-": {Direction.W, Direction.E},
        "7": {Direction.W, Direction.S},
        "J": {Direction.W, Direction.N},
        "F": {Direction.E, Direction.S},
        "L": {Direction.E, Direction.N},
        ".": set(),
        "S": set(Direction),
    }
    return d[char]


def find_start(maze):
    for i, line in enumerate(maze):
        j = line.find("S")
        if j >= 0:
            break
    assert maze[i][j] == "S"
    for d in Direction:
        di, dj = d.value
        if i + di < 0 or j + dj < 0 or i + di >= len(maze) or j + dj >= len(maze[0]):
            continue
        char = maze[i + di][j + dj]
        if d.reverse() in parse_pipe(char):
            return i, j, d


def move(maze, i, j, d):
    i += d.value[0]
    j += d.value[1]
    pipe = parse_pipe(maze[i][j])
    pipe.remove(d.reverse())
    d = pipe.pop()
    return i, j, d


def measure_maze(maze):
    i0, j0, d0 = find_start(maze)
    i, j, d = i0, j0, d0
    n = 0

    while True:
        i, j, d = move(maze, i, j, d)
        n += 1
        if i == i0 and j == j0:
            break

    return int(n / 2)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        maze = [line.rstrip() for line in input_file]
    print(measure_maze(maze))

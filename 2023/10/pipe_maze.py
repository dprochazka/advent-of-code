from enum import Enum


class Direction(Enum):
    N = (-1, 0)
    S = (1, 0)
    W = (0, -1)
    E = (0, 1)

    def reverse(self):
        return Direction((-self.value[0], -self.value[1]))

    def __str__(self):
        return self.name


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


def dir_to_pipe(chars):
    d = {
        "SN": "|",
        "NS": "|",
        "EW": "-",
        "WE": "-",
        "WS": "7",
        "SW": "7",
        "NW": "J",
        "WN": "J",
        "ES": "F",
        "SE": "F",
        "EN": "L",
        "NE": "L",
    }
    return d[chars]


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


def find_main_loop(maze):
    i0, j0, d0 = find_start(maze)
    i, j, d = i0, j0, d0
    pipes = [(i, j)]

    while True:
        i, j, d = move(maze, i, j, d)
        if i == i0 and j == j0:
            break
        pipes.append((i, j))

    return pipes


def clean_maze(maze, main_loop):
    new_maze = []
    for i, line in enumerate(maze):
        new_line = ""
        for j, char in enumerate(line):
            if (i, j) in main_loop:
                new_line += char
            else:
                new_line += "."
        new_maze.append(new_line)
    return new_maze


def measure_maze_inside(maze):
    inside_vol = 0
    for i, line in enumerate(maze):
        inside = False
        pipe_segment_start = None
        for j, char in enumerate(line):
            if char == "S":
                # complication: need to determine which char it is substituting
                directions = ""
                for d in Direction:
                    di, dj = d.value
                    if (
                        i + di < 0
                        or j + dj < 0
                        or i + di >= len(maze)
                        or j + dj >= len(maze[0])
                    ):
                        continue
                    char = maze[i + di][j + dj]
                    if d.reverse() in parse_pipe(char):
                        directions += str(d)
                char = dir_to_pipe(directions)
            if char == ".":
                if inside:
                    inside_vol += 1
            elif char == "|":
                # crossing vertical pipe
                inside = not inside
            elif char in "FL":
                # entered horizontal segment of pipe, e.g. '.F-J.'
                pipe_segment_start = char
            elif char in "J7":
                # escaped a horizontal segment of pipe
                if (pipe_segment_start == "F" and char == "J") or (
                    pipe_segment_start == "L" and char == "7"
                ):
                    # state change
                    inside = not inside
                pipe_segment_start = None
            else:
                pass
    return inside_vol


if __name__ == "__main__":
    with open("input.txt") as input_file:
        maze = [line.rstrip() for line in input_file]
    # part one
    print(measure_maze(maze))
    # part two
    main_loop = find_main_loop(maze)
    maze = clean_maze(maze, main_loop)
    print(measure_maze_inside(maze))

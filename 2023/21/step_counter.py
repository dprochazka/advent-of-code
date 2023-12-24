from collections import defaultdict, deque

START = "S"
GARDEN_PLOT = "."
ROCK = "#"

def parse_input(lines):
    return [list(l) for l in lines]

def step_counter(lines, steps):
    garden = parse_input(lines)
    queue = deque()
    visited = set()
    plots_steps = defaultdict(dict)
    steps_plots = defaultdict(list)
    for i, row in enumerate(garden):
        if START in row:
            queue.append((0, i, row.index(START)))
        
    def gen_step(i, j):
        M = len(garden)
        N = len(garden[0])
        for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
            if (
                not (0 <= i + di < M and 0 <= j + dj < N) or 
                (i+di, j+dj) in visited
            ):
                continue
            if garden[i+di][j+dj] in {START, GARDEN_PLOT}:
                yield i+di, j+dj

    while len(queue) > 0:
        n, i, j = queue.popleft()
        if n > steps:
            continue
        for i, j in gen_step(i, j):
            queue.append((n+1, i, j))
            visited.add((i, j))
            plots_steps[i][j] = n + 1
            steps_plots[n + 1].append((i, j))
    
    possible_plots = set()
    for n in range(steps % 2, steps + 1, 2):
        possible_plots |= set(steps_plots[n])

    return possible_plots

if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(len(step_counter(lines, 64)))

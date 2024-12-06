obstacles = set()
guard = tuple()  # i, j, di, dj

with open("input.txt") as input_file:
    for i, line in enumerate(input_file):
        for j, c in enumerate(line.rstrip()):
            if c == "#":
                obstacles.add((i, j))
            elif c == "^":
                guard = (i, j, -1, 0)
            elif c == ">":
                guard = (i, j, 0, 1)
            elif c == "v":
                guard = (i, j, 1, 0)
            elif c == "<":
                guard = (i, j, 0, -1)

M, N = i + 1, j + 1

#### Part1 ####
visited = set()

i, j, di, dj = guard
while 0 <= i < M and 0 <= j < N:
    visited.add((i, j))
    while (i + di, j + dj) in obstacles:
        di, dj = dj, -di  # turn right
    i, j = i + di, j + dj

print(len(visited))


#### Part2 ####
potential_sites = visited
potential_sites.remove((guard[0], guard[1]))

loop_cnt = 0
for i0, j0 in potential_sites:
    modified_obstacles = {(i0, j0)}.union(obstacles)
    seen_states = set()
    i, j, di, dj = guard
    while 0 <= i < M and 0 <= j < N:
        seen_states.add((i, j, di, dj))
        while (i + di, j + dj) in modified_obstacles:
            di, dj = dj, -di  # turn right
        i, j = i + di, j + dj
        if (i, j, di, dj) in seen_states:
            # been there, done that - a loop found!
            loop_cnt += 1
            break

print(loop_cnt)

import math

from haunted_wasteland import parse_input

with open("input.txt") as input_file:
    lines = [line.rstrip() for line in input_file]
    instructions, graph = parse_input(lines)


def move(node, step_number, instructions):
    return node[instructions[step_number % len(instructions)]]


def debug_ghosts(instructions, graph):
    for i, g in enumerate([node for node in graph.keys() if node[-1] == "A"]):
        print("GHOST ", i)
        pos = g
        print("start point", pos)
        print_next = 0
        for n in range(10**5):
            pos = move(graph[pos], n, instructions)
            if print_next:
                print(n, pos)
                print_next -= 1
            if pos[-1] == "Z":
                print(n, pos)
                print_next = 3


debug_ghosts(instructions, graph)

# it just so happens that the ghosts are already trapped in cycles at the start
# and it just so happens that each ghost has its own exit point

ghosts = [node for node in graph.keys() if node[-1] == "A"]
ghost_cycle_lenghts = []
for g in ghosts:
    pos = g
    n = 0
    while True:
        pos = move(graph[pos], n, instructions)
        n += 1
        if pos[-1] == "Z":
            ghost_cycle_lenghts.append(n)
            break
print(math.lcm(*ghost_cycle_lenghts))

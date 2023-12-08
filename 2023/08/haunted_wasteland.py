START_NODE = "AAA"
END_NODE = "ZZZ"


def parse_input(lines):
    instructions = list(map(lambda c: 0 if c == "L" else 1, lines.pop(0)))
    lines.pop(0)  # empty line

    def parse_line(l):
        node, edges = l.split(" = ")
        edges = tuple(edges.strip("()").split(", "))
        return node, edges

    graph = {k: v for k, v in map(parse_line, lines)}
    return instructions, graph


def find_path(instructions, graph):
    path = [START_NODE]
    i = 0
    while path[-1] != END_NODE:
        path.append(graph[path[-1]][instructions[i]])
        i += 1
        i %= len(instructions)
    return path


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(len(find_path(*parse_input(lines))) - 1)

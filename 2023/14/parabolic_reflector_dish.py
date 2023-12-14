def parabolic_reflector_dish(lines):
    load = 0
    for col in zip(*lines):
        s = -1  # location of current square rock or stopped round rock
        for i, c in enumerate(col):
            if c == "#":
                s = i
                continue
            if c == ".":
                continue
            if c == "O":
                s += 1
                load += len(col) - s
    return load


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(parabolic_reflector_dish(lines))

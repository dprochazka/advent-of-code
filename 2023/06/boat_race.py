import math


def find_solution_limits(race_time, record):
    lower = 0.5 * (race_time - math.sqrt(race_time**2 - 4 * record))
    upper = 0.5 * (race_time + math.sqrt(race_time**2 - 4 * record))
    return lower, upper

def find_number_of_ways_to_beat(race_time, record):
    lower, upper = find_solution_limits(race_time, record)
    # FIXME correction for whole number solutions
    if upper == math.floor(upper) or lower == math.floor(lower):
            return math.floor(upper) - math.floor(lower) - 1
    return math.floor(upper) - math.floor(lower)


def parse_input(lines):
    return {l.split(":")[0].lower(): map(int, l.split(":")[1].split()) for l in lines}

def solve_part_one(lines):
    times, records = parse_input(lines).values()
    return math.prod((
        find_number_of_ways_to_beat(t, r)
        for t, r in zip(times, records)
        ))

def solve_part_two(lines):
    times, records = parse_input(lines).values()
    megatime = int("".join((str(t) for t in times)))
    megarecord = int("".join((str(r) for r in records)))
    return find_number_of_ways_to_beat(megatime, megarecord)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(solve_part_two(lines))

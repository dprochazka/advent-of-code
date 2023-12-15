FACTOR = 17
BINS = 256


def hash_sequence(string):
    hashed = 0
    for c in string:
        hashed += ord(c)
        hashed *= FACTOR
        hashed %= BINS
    return hashed


def part_one(steps):
    return sum((hash_sequence(s) for s in steps))


def part_two(steps):
    hashmap = [{} for _ in range(BINS)]

    for s in steps:
        if "-" in s:
            label = s[:-1]
            i = hash_sequence(label)
            if label in hashmap[i]:
                del hashmap[i][label]
        elif "=" in s:
            label, focal = s.split("=")
            i = hash_sequence(label)
            hashmap[i][label] = int(focal)

    return sum(
        (
            i * n * f
            for i, box in enumerate(hashmap, start=1)
            for n, f in enumerate(box.values(), start=1)
        )
    )


if __name__ == "__main__":
    with open("input.txt") as input_file:
        steps = input_file.readline()[:-1].split(",")
    print(part_one(steps))
    print(part_two(steps))

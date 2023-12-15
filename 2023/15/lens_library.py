FACTOR = 17
BINS = 256


def hash_sequence(string):
    hashed = 0
    for c in string:
        hashed += ord(c)
        hashed *= FACTOR
        hashed %= BINS
    return hashed


if __name__ == "__main__":
    with open("input.txt") as input_file:
        steps = input_file.readline()[:-1].split(",")
    total = 0
    for s in steps:
        total += hash_sequence(s)
    print(total)

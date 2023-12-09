import numpy as np


def extrapolate_sequence(sequence: np.ndarray, backward=False):
    differences = [sequence]
    while True:
        diff = np.diff(differences[-1])
        if not np.any(diff):
            break
        differences.append(diff)
    pred = 0
    for diff in reversed(differences):
        if backward:
            pred = diff[0] - pred
        else:
            pred += diff[-1]
    return pred


def oasis(lines, version):
    if version not in {1, 2}:
        raise ValueError("Unknown version")
    predictions = []
    for line in lines:
        seq = np.fromstring(line, dtype=int, sep=" ")
        if version == 1:
            predictions.append(extrapolate_sequence(seq))
        if version == 2:
            predictions.append(extrapolate_sequence(seq, backward=True))
    return sum(predictions)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(oasis(lines, 2))

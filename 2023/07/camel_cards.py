COMBOS_VALUES = {
    "five-of-a-kind": 6 * 13**5,
    "four-of-a-kind": 5 * 13**5,
    "full-house": 4 * 13**5,
    "three-of-a-kind": 3 * 13**5,
    "two-pair": 2 * 13**5,
    "one-pair": 1 * 13**5,
}


def evaluate_hand(hand):
    # each value is a digit in base-13
    faces_val = {
        **{str(x): x - 2 for x in range(2, 10)},
        "T": 8,
        "J": 9,
        "Q": 10,
        "K": 11,
        "A": 12,
    }

    # value of cards only (without combos)
    value = sum(
        (faces_val[char] * 13**power for power, char in enumerate(reversed(hand)))
    )

    face_counts = sorted([hand.count(ch) for ch in faces_val.keys()], reverse=True)

    if face_counts[0] == 5:
        return COMBOS_VALUES["five-of-a-kind"] + value
    elif face_counts[0] == 4:
        return COMBOS_VALUES["four-of-a-kind"] + value
    if face_counts[0] == 3 and face_counts[1] == 2:
        return COMBOS_VALUES["full-house"] + value
    elif face_counts[0] == 3:
        return COMBOS_VALUES["three-of-a-kind"] + value
    elif face_counts[0] == 2 and face_counts[1] == 2:
        return COMBOS_VALUES["two-pair"] + value
    elif face_counts[0] == 2:
        return COMBOS_VALUES["one-pair"] + value
    else:
        return value


def evaluate_hand_part_two(hand):
    regular_faces = [
        *[str(x) for x in range(2, 10)],
        "T",
        "Q",
        "K",
        "A",
    ]
    faces_val = {"J": 0, **{f: i + 1 for i, f in enumerate(regular_faces)}}

    # value of cards only (without combos)
    value = sum(
        (faces_val[char] * 13**power for power, char in enumerate(reversed(hand)))
    )

    face_counts = [hand.count(ch) for ch in regular_faces]
    face_counts = sorted(face_counts, reverse=True)
    face_counts[0] += hand.count("J")

    if face_counts[0] == 5:
        return COMBOS_VALUES["five-of-a-kind"] + value
    elif face_counts[0] == 4:
        return COMBOS_VALUES["four-of-a-kind"] + value
    if face_counts[0] == 3 and face_counts[1] == 2:
        return COMBOS_VALUES["full-house"] + value
    elif face_counts[0] == 3:
        return COMBOS_VALUES["three-of-a-kind"] + value
    elif face_counts[0] == 2 and face_counts[1] == 2:
        return COMBOS_VALUES["two-pair"] + value
    elif face_counts[0] == 2:
        return COMBOS_VALUES["one-pair"] + value
    else:
        return value


def evaluate_game(lines, hand_evaluator):
    parsed_lines = sorted(
        [l.split() for l in lines],  # tuples hand, bet
        key=lambda x: hand_evaluator(x[0]),
    )
    return sum((rank * int(line[1]) for rank, line in enumerate(parsed_lines, start=1)))


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(evaluate_game(lines, evaluate_hand_part_two))

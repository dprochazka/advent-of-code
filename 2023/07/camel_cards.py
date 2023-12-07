def evaluate_hand(hand):
    combos_val = {
        "five-of-a-kind": 6,
        "four-of-a-kind": 5,
        "full-house": 4,
        "three-of-a-kind": 3,
        "two-pair": 2,
        "one-pair": 1,
        "high-card": 0,
    }

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

    if len(set(hand)) == len(hand):
        return combos_val["high-card"] * 13**5 + value
    if len(set(hand)) == len(hand) - 1:
        return combos_val["one-pair"] * 13**5 + value
    if len(set(hand)) == 1:
        return combos_val["five-of-a-kind"] * 13**5 + value

    face_counts = [hand.count(ch) for ch in faces_val.keys()]

    if max(face_counts) == 4:
        return combos_val["four-of-a-kind"] * 13**5 + value

    face_counts = sorted(face_counts, reverse=True)

    if face_counts[0] == 3 and face_counts[1] == 2:
        return combos_val["full-house"] * 13**5 + value
    elif face_counts[0] == 3:
        return combos_val["three-of-a-kind"] * 13**5 + value
    else:
        return combos_val["two-pair"] * 13**5 + value


def evaluate_game(lines):
    parsed_lines = sorted(
        [l.split() for l in lines],  # tuples hand, bet
        key=lambda x: evaluate_hand(x[0]),
    )
    return sum((rank * int(line[1]) for rank, line in enumerate(parsed_lines, start=1)))


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(evaluate_game(lines))

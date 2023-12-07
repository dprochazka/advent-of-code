from camel_cards import evaluate_game, evaluate_hand, evaluate_hand_part_two

EXAMPLE = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".splitlines()

EXPECTED_TOTAL_WINNINGS_PART_ONE = 6440
EXPECTED_TOTAL_WINNINGS_PART_TWO = 5905


def test_evaluate_game_part_one():
    assert evaluate_game(EXAMPLE, evaluate_hand) == EXPECTED_TOTAL_WINNINGS_PART_ONE


def test_evaluate_game_part_two():
    assert (
        evaluate_game(EXAMPLE, evaluate_hand_part_two)
        == EXPECTED_TOTAL_WINNINGS_PART_TWO
    )

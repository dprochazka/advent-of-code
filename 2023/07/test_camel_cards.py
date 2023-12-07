from camel_cards import evaluate_game

EXAMPLE = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

EXPECTED_TOTAL_WINNINGS = 6440


def test_evaluate_game():
    assert evaluate_game(EXAMPLE.splitlines()) == EXPECTED_TOTAL_WINNINGS

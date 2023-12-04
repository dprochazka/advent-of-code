def parse_card(card):
    _, numbers = card.split(":")
    winning_numbers, ticket_numbers = numbers.split("|")
    winning_numbers = [int(num) for num in winning_numbers.split()]
    ticket_numbers = [int(num) for num in ticket_numbers.split()]
    return winning_numbers, ticket_numbers


def count_winning_cards(winning_numbers, ticket_numbers):
    return sum((w in ticket_numbers for w in winning_numbers))


def evaluate_card(winning_numbers, ticket_numbers):
    count = count_winning_cards(winning_numbers, ticket_numbers)
    if count == 0:
        return 0
    return 2 ** (count - 1)


# Part One
def evaluate_pile_of_cards(cards):
    return [evaluate_card(*parse_card(c)) for c in cards]


# Part Two
def play_pile_of_cards(cards):
    card_copies = [1 for _ in range(len(cards))]
    for i, (copies, card) in enumerate(zip(card_copies, cards)):
        winning_cards = count_winning_cards(*parse_card(card))
        for j in range(winning_cards):
            card_copies[i + j + 1] += copies
    return card_copies


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(sum(evaluate_pile_of_cards(lines)))
    print(sum(play_pile_of_cards(lines)))

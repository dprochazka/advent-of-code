def parse_card(card):
    _, numbers = card.split(":")
    winning_numbers, ticket_numbers = numbers.split("|")
    winning_numbers = [int(num) for num in winning_numbers.split()]
    ticket_numbers = [int(num) for num in ticket_numbers.split()]
    return winning_numbers, ticket_numbers


def evaluate_card(winning_numbers, ticket_numbers):
    count = sum((w in ticket_numbers for w in winning_numbers))
    if count == 0:
        return 0
    return 2 ** (count - 1)


def evaluate_pile_of_cards(cards):
    return [evaluate_card(*parse_card(c)) for c in cards]


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(sum(evaluate_pile_of_cards(lines)))

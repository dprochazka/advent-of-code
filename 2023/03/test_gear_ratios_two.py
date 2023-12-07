import pytest

from test_gear_ratios import EXAMPLE, PART_NUMBERS, GEAR_RATIOS
from gear_ratios_two import Number, Symbol, parse_line, check_adjacency, find_part_numbers, find_gear_ratios


# def test_find_part_numbers():
#     found_numbers = find_part_numbers(EXAMPLE.splitlines())
#     assert set(found_numbers) == set(PART_NUMBERS)


@pytest.mark.parametrize(
    "line, expected",
    [
        ("%", {Symbol("%", 0)}),
        ("123", {Number("123", 0)}),
        (
            "%617*..12.#..0.1",
            {
                Symbol("%", 0),
                Symbol("*", 4),
                Symbol("#", 10),
                Number("617", 1),
                Number("12", 7),
                Number("0", 13),
                Number("1", 15),
            },
        ),
    ],
)
def test_parse_line(line, expected):
    assert set(parse_line(line)) == expected


@pytest.mark.parametrize(
    "sym, num, expected",
    [
        (Symbol("*", 3), Number("647", 0), True),
        (Symbol("*", 4), Number("647", 0), False),
        (Symbol("+", 5), Number("592", 2), True),
        (Symbol("+", 6), Number("592", 2), False),
        (Symbol("+", 0), Number("592", 1), True),
    ],
)
def test_check_adjacency(sym, num, expected):
    assert check_adjacency(num, sym) == expected

def test_find_part_numbers():
    found_numbers = find_part_numbers(EXAMPLE.splitlines())
    assert set(found_numbers) == set(PART_NUMBERS)


def test_find_gear_ratios():
    ratios = find_gear_ratios(EXAMPLE.splitlines())
    assert set(ratios) == set(GEAR_RATIOS)

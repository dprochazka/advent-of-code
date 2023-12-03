import pytest

from gear_ratios import find_part_numbers

EXAMPLE = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

PART_NUMBERS = [467, 35, 633, 617, 592, 755, 664, 598]


def test_find_part_numbers():
    found_numbers = find_part_numbers(EXAMPLE.splitlines())
    assert set(found_numbers) == set(PART_NUMBERS)

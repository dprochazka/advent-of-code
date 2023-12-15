import pytest
from point_of_incidence import find_all_mirrors, solve_part_two

EXAMPLE = [
"""
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
""".splitlines()[1:],
"""
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".splitlines()[1:]
]

EXPECTED = [5, 400]
EXPECTED_TWO = [300, 100]

@pytest.mark.parametrize(
    "block, expected",
    zip(EXAMPLE, EXPECTED)
)
def test_find_mirrors(block, expected):
    assert find_all_mirrors(block) == expected
 
@pytest.mark.parametrize(
    "block, expected",
    zip(EXAMPLE, EXPECTED_TWO)
)
def test_solve_part_two(block, expected):
    assert solve_part_two(block) == expected

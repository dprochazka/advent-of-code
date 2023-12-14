import pytest
from point_of_incidence import find_mirrors

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

@pytest.mark.parametrize(
    "block, expected",
    zip(EXAMPLE, EXPECTED)
)
def test_find_mirrors(block, expected):
    assert find_mirrors(block) == expected

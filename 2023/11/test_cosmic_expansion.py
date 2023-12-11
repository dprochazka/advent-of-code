from cosmic_expansion import parse_universe, measure_universe

EXAMPLE = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".splitlines()[1:]

EXPECTED = 374

MINI_EXAMPLE = """
.#...
#..#.
.....
.#.#.
""".splitlines()[1:]


def test_parse_universe():
    galaxies, empty_horizontal, empty_vertical = parse_universe(MINI_EXAMPLE)
    assert set(galaxies) == {(0, 1), (1, 0), (1, 3), (3, 1), (3, 3)}
    assert empty_horizontal == {2}
    assert empty_vertical == {2, 4}


def test_measure_universe():
    assert measure_universe(EXAMPLE) == EXPECTED

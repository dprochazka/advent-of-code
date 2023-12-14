from parabolic_reflector_dish import parabolic_reflector_dish

EXAMPLE = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".splitlines()[1:]

EXPECTED = 136

def test_parabolic_reflector_dish():
    assert parabolic_reflector_dish(EXAMPLE) == EXPECTED

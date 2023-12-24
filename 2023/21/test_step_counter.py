from step_counter import step_counter

EXAMPLE = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
""".splitlines()[1:]

def test_step_counter():
    assert len(step_counter(EXAMPLE, 6)) == 16

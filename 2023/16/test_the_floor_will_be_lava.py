import pytest
from the_floor_will_be_lava import count_energized, Direction

EXAMPLE = """
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
""".splitlines()[1:]


@pytest.mark.parametrize(
    "start, energized", [((0, 0, Direction.E), 46), ((0, 3, Direction.S), 51)]
)
def test_count_energized(start, energized):
    assert count_energized(EXAMPLE, start) == energized

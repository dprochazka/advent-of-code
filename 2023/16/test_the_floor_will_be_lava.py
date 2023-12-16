from the_floor_will_be_lava import count_energized

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

EXPECTED = 46

def test_count_energized():
    assert count_energized(EXAMPLE) == EXPECTED

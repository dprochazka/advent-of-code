from pipe_maze import measure_maze

EXAMPLE = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".splitlines()

EXPECTED = 8

def test_pipe_maze():
    assert measure_maze(EXAMPLE) == EXPECTED

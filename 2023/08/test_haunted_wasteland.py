import pytest

from haunted_wasteland import parse_input, find_path

EXAMPLE_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".splitlines()

EXAMPLE_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".splitlines()


def test_parse_input():
    assert parse_input(EXAMPLE_2) == (
        [0, 0, 1],
        {
            "AAA": ("BBB", "BBB"),
            "BBB": ("AAA", "ZZZ"),
            "ZZZ": ("ZZZ", "ZZZ"),
        },
    )


def test_find_path():
    assert (find_path(*parse_input(EXAMPLE_1))) == ["AAA", "CCC", "ZZZ"]


def test_find_path_length():
    assert (len(find_path(*parse_input(EXAMPLE_1)))) - 1 == 2
    assert (len(find_path(*parse_input(EXAMPLE_2)))) - 1 == 6

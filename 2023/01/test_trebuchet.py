import pytest

from trebuchet import parse_line


EXAMPLE = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

EXPECTED_VALUES = [12, 38, 15, 77]


@pytest.mark.parametrize(
    "input, expected",
    zip(EXAMPLE.splitlines(), EXPECTED_VALUES),
)
def test_parse_line(input, expected):
    assert parse_line(input) == expected

import pytest

from trebuchet import parse_line


EXAMPLE = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
foursixtwoninevtzzgntnlg6oneightbxp"""


EXPECTED_VALUES = [12, 38, 15, 77, 29, 83, 13, 24, 42, 14, 76, 48]


@pytest.mark.parametrize(
    "input, expected",
    zip(EXAMPLE.splitlines(), EXPECTED_VALUES),
)
def test_parse_line(input, expected):
    assert parse_line(input) == expected

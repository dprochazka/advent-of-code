from seeds import (
    parse_map,
    parse_inversed_map,
    find_locations_part_one,
    find_minimal_location_part_two,
)

EXAMPLE = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

SEED_RESULTS = [82, 43, 86, 35]

EXPECTED_MINIMAL_RESULT = 35

EXPECTED_RESULT_PART_TWO = 46


def test_parse_map():
    INPUT = """light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13"""
    m = parse_map(INPUT.splitlines())
    assert 1 == m(1)
    assert 37 == m(37)
    assert 45 == m(77)
    assert 46 == m(78)
    assert 50 == m(82)
    assert 67 == m(99)
    assert 68 == m(64)
    assert 80 == m(76)
    assert 81 == m(45)
    assert 99 == m(63)
    assert 100 == m(100)
    assert 101 == m(101)


def test_parse_inversed_map():
    INPUT = """light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13"""
    m = parse_inversed_map(INPUT.splitlines())
    assert m(1) == 1
    assert m(37) == 37
    assert m(45) == 77
    assert m(46) == 78
    assert m(50) == 82
    assert m(67) == 99
    assert m(68) == 64
    assert m(80) == 76
    assert m(81) == 45
    assert m(99) == 63
    assert m(100) == 100
    assert m(101) == 101


def test_find_locations():
    assert find_locations_part_one(EXAMPLE.splitlines()) == SEED_RESULTS


def test_find_minimal_location_part_two():
    find_minimal_location_part_two(EXAMPLE.splitlines()) == EXPECTED_RESULT_PART_TWO

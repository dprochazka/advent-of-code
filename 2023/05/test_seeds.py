from seeds import parse_map, find_locations

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


def test_find_locations():
    assert find_locations(EXAMPLE.splitlines()) == SEED_RESULTS

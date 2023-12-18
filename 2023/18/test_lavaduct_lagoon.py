from lavaduct_lagoon import measure_lagoon

EXAMPLE = """
""".splitlines()

EXPECTED = None

def test_measure_lagoon():
    assert measure_lagoon(EXAMPLE) == EXPECTED

import pytest
from pulse_propagation import pulse_propagation_one

EXAMPLE1 = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
""".splitlines()[1:]

EXAMPLE2 = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
""".splitlines()[1:]

EXPECTED1 = 32000000
EXPECTED2 = 11687500

@pytest.mark.parametrize(
        "example, expected", [(EXAMPLE1, EXPECTED1), (EXAMPLE2, EXPECTED2)]
)
def test_pulse_propagation(example, expected):
    assert pulse_propagation_one(example) == expected


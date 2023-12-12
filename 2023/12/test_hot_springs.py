import pytest
from hot_springs import bruteforce_hot_springs

EXAMPLE = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".splitlines()[1:]

EXPECTED = [1, 4, 1, 1, 4, 10]

@pytest.mark.parametrize(
    "line, combination",
    zip(EXAMPLE, EXPECTED)
)
def test_bruteforce_hot_springs(line, combination):
    assert bruteforce_hot_springs(line) == combination

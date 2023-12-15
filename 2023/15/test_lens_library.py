import pytest
from lens_library import hash_sequence, part_two

EXAMPLE = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")

EXPECTED = [30, 253, 97, 47, 14, 180, 9, 197, 48, 214, 231]

@pytest.mark.parametrize(
    "string, hashed",
    zip(EXAMPLE, EXPECTED)
)
def test_hash_sequence(string, hashed):
    assert hash_sequence(string) == hashed

def test_part_two():
    assert part_two(EXAMPLE) == 145

import pytest
import numpy as np
from mirage_maintenance import extrapolate_sequence

EXAMPLE = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

FORWARD_EXTRAPOLATIONS = [18, 28, 68]
BACKWARD_EXTRAPOLATIONS = [-3, 0, 5]


sequences = [np.fromstring(line, dtype=int, sep=" ") for line in EXAMPLE.splitlines()]


@pytest.mark.parametrize("seq, expected", zip(sequences, FORWARD_EXTRAPOLATIONS))
def test_extrapolate_sequence_forward(seq, expected):
    assert extrapolate_sequence(seq) == expected


@pytest.mark.parametrize("seq, expected", zip(sequences, BACKWARD_EXTRAPOLATIONS))
def test_extrapolate_sequence_backward(seq, expected):
    assert extrapolate_sequence(seq, backward=True) == expected

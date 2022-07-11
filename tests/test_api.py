import pytest

from lorempy.text import STANDARD, EXTENDED
from lorempy.api import full_text, extended_text, lorem


def test_full_text():
    """Test the full_text function."""
    assert full_text() == STANDARD

def test_extended_text():
    """Test the extended_text function."""
    assert EXTENDED == extended_text()


@pytest.mark.parametrize("index", list(range(1000)))
def test_lorem(index):
    """Test the lorem function call."""
    assert isinstance(index, int)
    assert lorem() in STANDARD

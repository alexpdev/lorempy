from lorempy.text import STANDARD, EXTENDED
import pytest

def splitExt():
    """Split EXTENDED into individual words."""
    return EXTENDED.split(" ")

pytest.fixture
def standard():
    """Test fixture for the standard text."""
    text = STANDARD.split(" ")
    return text

def test_standard(standard):
    """Test the constant STANDARD."""
    assert "lorem" in standard

@pytest.mark.parametrize("word", splitExt())
def test_extended(word):
    """Test the constant EXTENDED."""
    assert word in EXTENDED

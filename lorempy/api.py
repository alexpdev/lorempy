from itertools import cycle
from lorempy.text import STANDARD, EXTENDED

def full_text():
    """Return the full standard text."""
    return STANDARD

def extended_text():
    """Return the orignal extended text."""
    return EXTENDED

class GenClass:
    """Generator class for yielding lorem words."""

    def __init__(self):
        """Initialize GenClass class."""
        self.standard_words = STANDARD.split(" ")
        self.extended_words = EXTENDED.split(" ")
        self._gen = cycle(self.standard_words)
        self._exgen = cycle(self.extended_words)

    @property
    def lorem(self):
        """Return next word of sequence."""
        return next(self._gen)

class Lorem:
    """Namespace for Lorem obfuscation and abstraction."""
    this = GenClass()

    @classmethod
    def lorem(cls):
        """Class method for generating next word of lorem sequence."""
        return cls.this.lorem

def lorem():
    """Further abstraction of generating next word of lorem sequence."""
    return Lorem.lorem()

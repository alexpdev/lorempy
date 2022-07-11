# LoremPy

Library for generating the standard dummy text "Lorem ipsum dolar..."

## Usage

To use LoremPy in your project:

```python
import lorempy
# or
from lorempy import lorem, full_text
# or
from lorempy import *
```

## API

### Functions

> lorem 
>> Generates one word from the lorem ipsum seq in order and repeats forever.

> full_text
>> Returns the full lorem ipsum sequence as one string.

```python
text = lorempy.full_text()
word = lorempy.lorem()
```

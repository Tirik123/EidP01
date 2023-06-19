from   dataclasses import dataclass
from   typing      import Any, Optional, Union
import math
import pytest

## Aufgabe 8 (Functional Programming) ##########################################

def twice(f):
    return lambda x: f(f(x))

def pythagorean_triples(n):
    return [ (x, y, z) for x in range(1, n)
                       for y in range(x, n)
                       for z in range(y, n)
                       if x ** 2 + y ** 2 == z ** 2 ]
from   dataclasses import dataclass
from   typing      import Any, Optional, Union
import math
import pytest

## Aufgabe 7 (Generators) ######################################################

def my_enumerate(xs):
    i = 0
    for x in xs:
        yield (i, x)
        i += 1

def prefixes(xs):
    for i in range(len(xs)+1):
        yield xs[:i]

def alternate(xs, ys):
    try:
        while True:
            yield next(xs)
            xs, ys = ys, xs
    except:
        yield from ys
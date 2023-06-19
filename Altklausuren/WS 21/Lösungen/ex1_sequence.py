from   dataclasses import dataclass
from   typing      import Any, Optional, Union
import math
import pytest

## Aufgabe 1 (Sequence) ########################################################

def count_iterations(n: int) -> int:
    count = 0
    while n != 0:
        if n % 3 == 0:
            n = n + 4
        else:
            if (n % 3 != 0) and (n % 4 == 0):
                n = n // 2
            else:
                n = n - 1
        count += 1
    return count

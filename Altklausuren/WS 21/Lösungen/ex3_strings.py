from   dataclasses import dataclass
from   typing      import Any, Optional, Union
import math
import pytest

## Aufgabe 3 (Strings) #########################################################

def is_strong(pw: str) -> bool:
    specials = ['!', '?', '+', '*']
    if len(pw) < 8:
        return False
    intCount = 0
    upperCount = 0
    usedSpecials = []

    for c in pw:
        if c in specials:
            usedSpecials += [c]
        elif c.isupper():
            upperCount += 1
        elif c.isdigit():
            intCount += 1

    if intCount < 1:
        return False
    elif intCount <= 3:
        if len(usedSpecials) > 0:
            usedSpecials.pop(0)
        else:
            return False
    
    if upperCount < 3:
        if len(usedSpecials) > 0:
            usedSpecials.pop(0)
        else:
            return False
    return True
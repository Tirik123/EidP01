from   dataclasses import dataclass
from   typing      import Any, Optional, Union
import math
import pytest

def is_prime(n: int) -> bool:
  if n == 2:
      return True
  elif n < 2 or n % 2 == 0:
      return False
  else:
      x = math.floor(math.sqrt(n)) + 1
      i = 3
      while i < x:
          if n % i == 0:
              return False
          i += 2
      return True

## Aufgabe 5 (Tests) ###########################################################

def test_isPrime1():
    assert not is_prime(1)

def test_isPrime2():
    assert is_prime(2)

def test_isPrime3():
    assert not is_prime(9)

def test_isPrime4():
    assert is_prime(11)

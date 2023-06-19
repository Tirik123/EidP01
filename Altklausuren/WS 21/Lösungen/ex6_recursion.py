from   dataclasses import dataclass
from   typing      import Any, Optional, Union
import math
import pytest

@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']

## Aufgabe 6 (Recursion) #######################################################
# Hinweis: achtet auf Pre-Order

def find_substrings(node: Node, substr: str) -> list[str]:
    tmp = []
    if substr in node.mark:
        tmp.append(node.mark)
    if node.left != None:
        tmp += find_substrings(node.left, substr)
    if node.right != None:
        tmp += find_substrings(node.right, substr)
    return tmp
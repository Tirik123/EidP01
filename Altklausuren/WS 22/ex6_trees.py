# Aufgabe 6 (Rekursion) #######################################################

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']


Tree = Optional[Node]


# (a) #########################################################################

# def mark_at_path(tree, path):


# (b) #########################################################################

# def paths(tree):

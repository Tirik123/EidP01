from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']


def find_substrings()
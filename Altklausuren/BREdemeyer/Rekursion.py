from typing import Optional
from dataclasses import dataclass

@dataclass
class BinaryNode:
    mark: float
    left: Optional["BinaryNode"]
    right: Optional["BinaryNode"]



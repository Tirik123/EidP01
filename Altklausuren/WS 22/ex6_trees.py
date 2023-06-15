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

def mark_at_path(tree: Tree, path: str) -> Optional[str]:
    if tree is None:
        return None
    if path == "":
        return tree.mark
    if path[0] == "l":
        return mark_at_path(tree.left, path[1:])
    if path[0] == "r":
        return mark_at_path(tree.right, path[1:])
    
    


# (b) #########################################################################

def paths(tree: Tree) -> list[str]:
    if tree is None:
        return []
    ps = [""]
    for p in paths(tree.left):
        ps.append("l" + p)
    for p in paths(tree.right):
        ps.append("r" + p)
    return ps



example = Node("n0",Node("n1", None, None),Node("n2",Node("n3", None, None),Node("n4", None, None)))


if __name__ == "__main__":
    assert mark_at_path(example, "") == "n0"
    assert mark_at_path(example, "l") == "n1"
    assert mark_at_path(example, "r") == "n2"
    assert mark_at_path(example, "rl") == "n3"
    assert mark_at_path(example, "rr") == "n4"
    assert mark_at_path(example, "ll") is None

    assert paths(example) == ["", "l", "r", "rl", "rr"]

    



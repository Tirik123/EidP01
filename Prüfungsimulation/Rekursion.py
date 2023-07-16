from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']

Tree = Optional[Node] # Trees can be empty


def mark_at_path(tree: Tree, path: str):
    if path == "":
        return "n0"
    for i in path:
        if i == 'l':
            mark_at_path(tree.left, i)
        if i == 'r':
            mark_at_path(tree.right, i)
    return tree
    
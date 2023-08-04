from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']


Tree = Optional[Node]


example = Node("n0",
            Node("n1", None, None),
            Node("n2",
                Node("n3", None, None),
                Node("n4", None, None)
            )
        )    



#a)

def mark_at_path(tree: Tree, path: str) -> Optional[str]:
    if tree is None:
        return None
    if path == '':
        return tree.mark
    if path[0] == 'l':
        return mark_at_path(tree.left, path[1:])
    if path[0] == 'r':
        return mark_at_path(tree.right, path[1:])


#b)

def paths(tree: Tree) -> list[str]:
    if tree is None:
        return []
    ps = [""]
    for p in paths(tree.left):
        ps.append("l" + p)
    for p in paths(tree.right):
        ps.append("r" + p)
    return ps
    


        


if __name__ == '__main__':
    print(mark_at_path(example, ""))
    print(mark_at_path(example, "rl"))
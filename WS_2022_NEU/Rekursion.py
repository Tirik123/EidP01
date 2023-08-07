from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']


Tree = Optional[Node] # Trees can be empty.


def mark_at_path(tree: Tree, path: str) -> Optional[str]:
    if tree is None:
        return None
    elif path == '':
        return tree.mark
    elif path[0] == 'l':
        if tree.left is not None:
            return mark_at_path(tree.left, path[1:])
    elif path[0] == 'r':
        if tree.right is not None:
            return mark_at_path(tree.right, path[1:])
    



def paths(tree: Tree, path: str = '') -> list[str]:
    if tree is None:
        return []

    # Wenn der aktuelle Knoten ein Blattknoten ist, füge den aktuellen Pfad zur Liste aller Pfade hinzu
    if tree.left is None and tree.right is None:
        return [path]

    # Rekursiv den linken und rechten Teilbaum durchlaufen und die Pfade zusammenführen
    left_paths = paths(tree.left, path + 'l')
    right_paths = paths(tree.right, path + 'r')
    return [path] + left_paths + right_paths

# Beispielbaum
example = Node("n0",
               Node("n1", None, None),
               Node("n2",
                    Node("n3", None, None),
                    Node("n4", None, None)
                    )
               )


if __name__ == '__main__':
    example = Node("n0",
                Node("n1", None, None),
                Node("n2",
                    Node("n3", None, None),
                    Node("n4", None, None)
                )
            )
    print(mark_at_path(example, 'rl'))

    print(paths(example))
    

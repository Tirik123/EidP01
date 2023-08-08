from dataclass import dataclass
from typing import Optional


@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']


def layer(n: int, node: Node) -> list[Node]:
    result = []
    if node.mark is not None:
        if str(n) in node.mark:
            result.append(node.mark)
    if node.left is not None:
        result += layer(n, node.left)
    if node.right is not None:
        result += layer(n, node.right)
    return result


if __name__ == '__main__':
    tree = Node('0', Node('1a', None, Node('2', None, None)), Node('1b', None, None))
    print(layer(2, tree))


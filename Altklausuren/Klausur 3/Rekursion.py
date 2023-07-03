from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']



def layer(n: int, node: Node) -> list:
    if n == 0:
        return [node.mark]
    result = []
    if node.left:
        result.append(layer(n - 1, node.left))
    if node.right:
        result.append(layer(n - 1, node.right))
    flattened_result = [item for sublist in result for item in sublist]
    return flattened_result

    



if __name__ == '__main__':
    tree = Node('0', Node('1a', None, Node('2', None, None)),
                Node('1b', None, None))
    print(layer(0, tree))
    print(layer(1, tree))
    print(layer(2, tree))
     
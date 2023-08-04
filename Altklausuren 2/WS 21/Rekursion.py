from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']


def find_substrings(node: Node, substr: str) -> list[str]:
    if node is None:
        return []
    result = []
    if node.mark is not None:
        if substr in node.mark:
            result.append(node.mark)
    if node.left is not None:
        result += find_substrings(node.left, substr)
    if node.right is not None:
        result += find_substrings(node.right, substr)
    return result


if __name__ == '__main__':
    tree = Node("aab", Node("baa", None, None), Node("aba", None, None))
    print(find_substrings(tree, 'ab'))
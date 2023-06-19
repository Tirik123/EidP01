from dataclasses import dataclass
from typing import Optional


# Pre-Order: Mark, Left, Right

@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']


def find_substrings(node: Node, substr: str) -> list[str]:
    new_list = []
    if substr in node.mark:
        new_list.append(node.mark)
    if node.left != None:
        new_list += find_substrings(node.left, substr)
    if node.right != None:
        new_list += find_substrings(node.right, substr)
    return new_list
    
if __name__ == '__main__':
    tree = Node("aab", Node("baa", None, None), Node("aba", None, None))
    print(find_substrings(tree, 'ab'))
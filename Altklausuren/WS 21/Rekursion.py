from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']



def find_substrings(node: Node, substr: str) -> list[Node]:
    result = []
    if substr in node.mark:
        result.append(node.mark)
    if node.left is not None:
        result += find_substrings(node.left, substr)
    if node.right is not None:
        result += find_substrings(node.right, substr)
    return result



def find_substrings_in_order(node: Node, substr: str) -> list[Node]:
    result = []
    if node.left is not None:
        result += find_substrings(node.left, substr)
    if substr in node.mark:
        result.append(node.mark)
    if node.right is not None:
        result += find_substrings(node.right, substr)
    return result

if __name__ == '__main__':
    tree = Node("aab", Node("baa", None, None), Node("aba", None, None))
    #print(find_substrings(tree, 'ab'))
    print(find_substrings_in_order(tree, 'a'))

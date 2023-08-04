from dataclasses import dataclass
from typing import Optional
@dataclass
class Node:
    mark: str   
    left: Optional['Node']
    right: Optional['Node']



def find_substrings(node: Node, substr: str) -> list[str]:
    result = []
    if substr in node.mark:
        result.append(node.mark)
    if node.left is not None:
        pass
    if node.right is not None:
        pass
    return result



if __name__ == '__main__':
    tree = Node("aab", 
                Node("baa", None, None), 
                Node("aba", None, None))
    print(find_substrings(tree, 'ab'))
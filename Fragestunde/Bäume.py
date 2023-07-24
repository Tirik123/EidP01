from dataclasses import dataclass
from typing import Optional

@dataclass  #Baumstruktur immer vorgegeben
class Node:
    mark: str
    left: Optional["Node"]  # das gleiche wie 'Node' | None, ABER: Optional ist immer 'Node' oder None
    right: Optional['Node']    # das gleiche wie Optional['Node'] -> '' sind wichtig. Kann auch 'Node' | float sein z.B.


Tree = Node | None

tree = Node('*',
            Node('+',
                 Node('1', None, None),
                 Node('1', None, None)),
                 Node('2', None, None)
)


def to_str(tree: Tree) -> str:
    if tree is None:    # Basisfall wenn tree None ist = leerer Baum
        return ''
    if tree.left is None and tree.right is None:    # Wenn mark keine Kinder hat, dann nur den mark ohne Klammern ausgeben 
        return tree.mark
    return "(" + to_str(tree.left) + tree.mark + to_str(tree.right) + ")"   #Rekursion


#selbe Fnktion mit Pattern matching

def to_str_pattern(tree: Tree) -> str:
    match tree:
        case None:
            return ''
        case Node(mark, None, None):
            return mark
        case Node(mark, left, right):
            return '(' + to_str_pattern(left) + mark + to_str_pattern(right) + ')'


# Schema sehr wichtig -> großes Problem, das wird aufgeteilt und zusammengefügt. Basisfall/Basisfälle wichtig

if __name__ == '__main__':
    print(to_str(tree))
    print(to_str_pattern(tree))


#Rekursionsaufgabe immer gleich aufgebaut: Basisfall + Rekursion

#Rekursion: am Bsp Fakultät

# 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4!
# n! = n * (n - 1)!

def f(n: int) -> int:
    if n == 0:  #Basisfall 
        return 1
    return n * f(n - 1) # Rekursion

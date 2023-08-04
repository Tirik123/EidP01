from typing import Optional
from dataclasses import dataclass

@dataclass
class BinaryNode:
    mark: float
    left: Optional["BinaryNode"]
    right: Optional["BinaryNode"]

    def invert(self):
        if self.left is not None:
            self.left.invert()
        if self.right is not None:
            self.right.invert()
        self.left, self.right = self.right, self.left


    def weight(self) -> float:
        result = self.mark
        if self.left is not None:
            result += self.left.weight()
        if self.right is not None:
            result += self.right.weight()
        return result
    

    def __repr__(self) -> str:
        ...
    
    

def height(tree: BinaryNode):
    height_left = 1
    height_right = 1
    if tree is None:
        return 0
    if tree.left is not None:
        height_left += 1
        height(tree.left)
    if tree.right is not None:
        height_right += 1
        height(tree.right)
    return max(height_left, height_right)
        



if __name__ == '__main__':
    '''tree = BinaryNode(
    2.5,
    BinaryNode(
        9.4,
        BinaryNode(0.4, None, None),
        None
    ),
    BinaryNode(1.7, None, None),
    )

    inverted_tree = BinaryNode(
    2.5,
    BinaryNode(1.7, None, None),
    BinaryNode(
        9.4,
        None,
        BinaryNode(0.4, None, None)
        ),
    )


    tree.invert()

    assert tree == inverted_tree'''



    '''tree = BinaryNode(
    2.5,
    BinaryNode(
        9.4,
        BinaryNode(0.4, None, None),
        None
    ),
    BinaryNode(1.7, None, None),
)

    print(tree.weight())
    assert tree.weight() == 14.0

'''
    tree = BinaryNode(
    2.5,
    BinaryNode(
        9.4,
        BinaryNode(0.4, None, BinaryNode(1.0, None, None)),
        None
    ),
    BinaryNode(1.7, None, None),
)

    assert height(tree) == 2
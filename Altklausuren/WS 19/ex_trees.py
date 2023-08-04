class Tree:
    def __init__(self, mark, children: list):
        self.mark = mark    # int
        self.children = children    #list[Optional['Tree']]

    def marks(self) -> list[int]:
        result = []
        result.append(self.mark)
        for i in self.children:
            result.append(i.marks())
        return result
    
    def map(self, f):
        new_children = [child.map(f) for child in self.children]
        return Tree(f(self.mark), new_children)
    
    def __repr__(self):
        return f"Tree({self.mark}, {self.children})"
    


if __name__ == '__main__':
    t = Tree(0, [
        Tree(1, []),
        Tree(2, [
                Tree(3, []),
                Tree(4, []),
                Tree(5, [])
            ])
        ])
    
    #print(t.marks())

    print(t.map(lambda x: x * 2))
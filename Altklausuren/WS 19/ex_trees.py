class Tree:
    def __init__(self, mark, children: list):
        self.mark = mark
        self.children = children

    def marks(self) -> list:
        marks = [self.mark]
        for c in self.children:
            marks = marks + c.marks()
        return marks



t = Tree(0, [
            Tree(1, []),
            Tree(2, [
                Tree(3, []),
                Tree(4, []),
                Tree(5, [])
            ])
        ])




if __name__ == '__main__':
    print(t.marks())
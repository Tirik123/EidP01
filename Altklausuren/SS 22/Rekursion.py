from dataclasses import dataclass

@dataclass
class TextNode:
    text: str


@dataclass
class ElemNode:
    name: str
    children: list['Node']

Node = TextNode | ElemNode


def node_to_str(node: Node) -> str:
    if type(node) is TextNode:
        return node.text
    elif type(node) is ElemNode:
        for child in node.children:
            return '<' + node.name + '>' + node_to_str(child) + '</' + node.name + '>'
        

if __name__ == '__main__':
    print(node_to_str(ElemNode('b', [TextNode('important')])))
    print(node_to_str(TextNode('important')))
    print(node_to_str(ElemNode('b', [TextNode('important')])))
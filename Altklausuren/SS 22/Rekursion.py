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
        result = "<" + node.name + ">"
        for child in node.children:
            result += node_to_str(child)
        result += "<" + node.name + "/>"
        return result
        

if __name__ == '__main__':
    print(node_to_str(ElemNode('b', [])))
    #print(node_to_str(TextNode('important')))
    #print(node_to_str(ElemNode('b', [TextNode('important')])))
    print(node_to_str(ElemNode('p', [
                                    TextNode('It is very '),
                                    ElemNode('b', [
                                    TextNode('important'),
                                    ]),
                                    TextNode(' to pay attention.'),
                                    ])))
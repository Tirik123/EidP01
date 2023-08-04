from dataclasses import dataclass


@dataclass
class TextNode:
    text: str


@dataclass
class ElemNode:
    name: str
    children: list["Node"]


Node = TextNode | ElemNode


def node_to_str(node: Node) -> str:
    result = ''
    match node:
        case TextNode(text):
            return text
        case ElemNode(name, children):        
            result += '<' + name + '>'
            for i in children:
                result += node_to_str(i)
            return result + '</' + name + '>'
        


#b)

def p(*args):
    if type(Node) == TextNode:
        for p in args:
            node_to_str(p)
        
        


if __name__ == '__main__':
    #print(node_to_str(TextNode('important')))
    #print(node_to_str(ElemNode('b', [])))
    #print(node_to_str(ElemNode("b", [TextNode('important')])))
    print(node_to_str(ElemNode('p', [TextNode('It is very '), ElemNode('b', [TextNode('important')]), TextNode(' to pay attention')])))
    assert p() == ElemNode('p', [])
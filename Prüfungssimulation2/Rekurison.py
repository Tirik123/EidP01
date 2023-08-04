from dataclasses import dataclass


@dataclass
class TextNode:
    text: str


@dataclass
class ElemNode:
    name: str
    children: list['Node']


Node = TextNode | ElemNode

# a)


def node_to_str(node: Node) -> str:
    result = ''
    match node:
        case TextNode(text):
            result += text
        case ElemNode(name, children):
            result += '<' + name + '>'
            for i in children:
                result += node_to_str(i)
            result += '</' + name + '>'
    return result


if __name__ == '__main__':
    print(node_to_str(TextNode('important')))
    print(node_to_str(ElemNode('b', [])))
    print(node_to_str(ElemNode('b', [TextNode('important')])))
    print(node_to_str(
        ElemNode('p', [
            TextNode('It is very '),
            ElemNode('b', [
                TextNode('important'),
            ]),
            TextNode(' to pay attention'),
        ])
    ))


# 10/10
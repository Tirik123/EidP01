from tree import Node, Var, Val, Op, OpSym
from typing import Any

def node_to_str(Tree: Node) -> str:
    match Tree:
        case Var(x):
            return x
        case Val(i):
            return str(i)
        case Op(s, l, r):
            return ('(' + node_to_str(l) + ' ' + s.value + ' ' + node_to_str(r) + ')')
        case _:
            raise Exception("unreachable")
        


def node_to_str_if(Tree: Node) -> str:
    if type(Tree) is Var:
        return Tree.name
    elif type(Tree) is Val:
        return str(Tree.value)
    elif type(Tree) is Op:
        return ('(' + node_to_str_if(Tree.left) + ' ' + Tree.sym.value + ' ' + node_to_str_if(Tree.right) + ')')
    else:
        raise Exception('unreachable')
    

'''def node_to_str_if(Tree: Node) -> str:
    if type(Tree) is Val:
        return str(Tree.value)
    elif type(Tree) is Var:
        return Tree.name
    elif type(Tree) is Op:
        return ('(' + node_to_str_if(Tree.left) +
                ' ' + Tree.sym.value +
                ' ' + node_to_str_if(Tree.right) +
                ')')
    else:
        raise Exception("unreachable")'''
    

def optimize_step(e: Node) -> Any:
    match e:
        case Op(OpSym.ADD, Val(l), Val(r)):
            return Val(l + r)
        case Op(OpSym.MUL, Val(l), Val(r)):
            return Val(l * r)
        case Op(OpSym.ADD, e1, e2) if e1 == e1:
            return Op(OpSym.MUL, Val(2), e1)
        






if __name__ == '__main__':
    e = Op(OpSym.ADD, Op(OpSym.MUL, Val(2), Var('x')), Val(5))
    assert node_to_str(e) == '((2 * x) + 5)'
    assert node_to_str(Var('x')) == 'x'
    assert node_to_str(Val(2)) == '2'



#Tree:

'''class OpSym(Enum):
    ADD = "+"
    MUL = "*"


@dataclass
class Var:
    name: str


@dataclass
class Val:
    value: int


@dataclass
class Op:
    sym: OpSym
    left: 'Node'
    right: 'Node'''

#Node = Var | Val | Op
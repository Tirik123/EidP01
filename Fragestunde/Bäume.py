from dataclasses import dataclass
from typing import Optional

@dataclass  #Baumstruktur immer vorgegeben
class Node:
    mark: str
    left: Optional["Node"]  # das gleiche wie 'Node' | None
    right: 'Node' | None    # das gleiche wie Optional['Node'] -> '' sind wichtig 


Tree = Node | None

Tree = Node('1',
            Node("2", None, None),
            Node('3',
                 Node("4", None, None),
                 None)
                 )



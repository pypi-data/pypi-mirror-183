from typing import Optional
from .klass import TagInstance, Enviroment
from dataclasses import dataclass

@dataclass
class Node:
    l: int
    c: int
    
    def execute(self, env: Enviroment) -> TagInstance: # type: ignore
        pass

@dataclass
class NLiteral(Node):
    value: str | int | float

@dataclass
class NArray(Node):
    value: list[Node]

@dataclass
class NArithmetic(Node):
    left: Node
    op: str
    right: Node

@dataclass
class NUnary(Node):
    op: str
    value: Node

@dataclass
class NCmp(Node):
    left: Node
    op: str
    right: Node

@dataclass
class NDo(Node):
    tree: list[Node]

@dataclass
class NSetVar(Node):
    name: str
    value: Node

@dataclass
class NGetVar(Node):
    name: str

@dataclass
class NDot(Node):
    left: Node
    right: str

@dataclass
class NCall(Node):
    caller: Node
    args: list[Node]
    argk: dict[str, Node]

@dataclass
class NFieldSet(Node):
    origin: str
    field: list[str]
    value: Node

@dataclass
class NIfElse(Node):
    cond: Node
    body: Node
    elif_: list['NElif']
    else_: Optional['NElse']

@dataclass
class NElif(Node):
    cond: Node
    body: Node

@dataclass
class NElse(Node):
    body: Node

@dataclass
class NWhile(Node):
    cond: Node
    body: Node

@dataclass
class NFor(Node):
    name: str
    value: Node
    body: Node
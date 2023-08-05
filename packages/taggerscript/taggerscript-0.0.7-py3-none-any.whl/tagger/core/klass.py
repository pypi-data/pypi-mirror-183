from typing import Optional
import typing
from .error import Error

TagArg = list['TagInstance']
Kargs = dict[str, 'TagInstance']

class TagClass:
    NAME = "BaseClass"
    
    # def new(self):
    #     t = TagInstance()
    #     t.type = self
    #     return t
    
    def repr(self, this: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    
    def add(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def sub(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def mult(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def div(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    
    def pos(self, this: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def neg(self, this: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def notb(self, this: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    
    def gt(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def lt(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def gteq(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def lteq(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def equal(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def nequal(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def andl(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    def orl(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    
    def bool(self, this: 'TagInstance') -> 'TagInstance': # type: ignore
        pass
    
    def call(self, this: 'TagInstance', args: TagArg, kargs: Kargs, env: 'Enviroment') -> 'TagInstance': # type: ignore
        pass
    
    def iter(self, this: 'TagInstance') -> typing.Generator['TagInstance', typing.Any, None]: # type: ignore
        pass
    
    def __repr__(self) -> str:
        return self.NAME
    
    def _bool_(self, this: 'TagInstance') -> 'bool': # type: ignore
        return True

class TagInstance:
    
    def __init__(self) -> None:
        self.type: TagClass
        self.field: dict[str, TagInstance] = {}
    
    def set_type(self, t: TagClass):
        self.type = t
    
    def istype(self, klass: type):
        return isinstance(self.type, klass)
    
    def add(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.add(self, right)
    def sub(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.sub(self, right)
    def mult(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.mult(self, right)
    def div(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.div(self, right)

    def gt(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.gt(self, right)
    def gteq(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.gteq(self, right)

    def lt(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.lt(self, right)
    def lteq(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.lteq(self, right)

    def equal(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.equal(self, right)
    def nequal(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.nequal(self, right)

    def andl(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.andl(self, right)
    def orl(self, right: 'TagInstance') -> 'TagInstance':
        return self.type.orl(self, right)
    
    def bool(self) -> 'TagInstance':
        return self.type.bool(self)
    
    def _bool_(self) -> 'bool': # type: ignore
        return self.type._bool_(self)
    
    def pos(self) -> 'TagInstance':
        return self.type.pos(self)
    def neg(self) -> 'TagInstance':
        return self.type.neg(self)
    def notb(self) -> 'TagInstance':
        return self.type.notb(self)
    
    def call(self, args: TagArg, kargs: Kargs, env: 'Enviroment') -> 'TagInstance':
        return self.type.call(self, args, kargs, env)
    
    def iter(self) -> typing.Generator['TagInstance', typing.Any, None]:
        yield from self.type.iter(self)
    
    def repr(self) -> 'TagInstance':
        return self.type.repr(self)
    
    def __repr__(self) -> str:
        return self.repr().__repr__()


class Enviroment:
    
    def __init__(self, parent: Optional['Enviroment']=None) -> None:
        self.parent = parent
        self.table: dict[str, TagInstance] = {}
        self.error: list[Error] = []
    
    def throw(self, err: str, msg: str, l: int, c: int):
        self.error.append(Error(err, msg, l, c))

    def get(self, n: str):
        if n not in self.table:
            if self.parent:
                return self.parent.get(n)
        return self.table.get(n)
    
    def set(self, n: str, v: TagInstance):
        self.table[n] = v
    
    def __iter__(self):
        yield from self.table.items()
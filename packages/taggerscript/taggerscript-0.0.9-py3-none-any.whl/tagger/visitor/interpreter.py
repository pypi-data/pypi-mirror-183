from tagger.core.node import Node
from .tag_builtin import *
from .obj_builtin import *
from . import executor # DO NOT REMOVE. this module initialize all Node execute method 

class TagInterpreter:
    
    def __init__(self) -> None:
        self.globalenv = Enviroment()
        self.globalenv.set('print', TagFunction('print', print_))
        self.globalenv.set('Table', Table)
        self.globalenv.set('slice', TagFunction('slice', slice_))
    
    def start(self, n: Node):
        self.globalenv.error.clear()
        e = n.execute(self.globalenv)
        if not e:
            return
        if e.istype(TagBaseException):
            er = typing.cast(TagException, e)
            self.globalenv.throw(er.error, er.msg, n.l, n.c)
            return
        return e
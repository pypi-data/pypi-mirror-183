import asyncio
from core.klass import *
import typing

class TagBase(TagClass):
    NAME = "Base"
    
    def __init__(self) -> None:
        super().__init__()
    
    def add(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return make_error("TypeError", f"{self.NAME} + {right.type} is not supported")
    def sub(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return make_error("TypeError", f"{self.NAME} - {right.type} is not supported")
    def mult(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return make_error("TypeError", f"{self.NAME} * {right.type} is not supported")
    def div(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return make_error("TypeError", f"{self.NAME} / {right.type} is not supported")
    
    def gt(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return TagInteger(0)
    def gteq(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return TagInteger(0)
    def lt(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return TagInteger(0)
    def lteq(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return TagInteger(0)
    
    def equal(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return TagInteger(int(this.field == right.field))
    def nequal(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return TagInteger(int(not typing.cast(TagInteger, this.equal(right)).bool()))
    
    def pos(self, this: 'TagInstance'):
        return make_error("TypeError", f"{self.NAME} cannot do unary addition operation")
    def neg(self, this: 'TagInstance'):
        return make_error("TypeError", f"{self.NAME} cannot do unary subtration operation")
    def notb(self, this: 'TagInstance'):
        return TagInteger(int(not this.bool()))
    
    def andl(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return TagInteger(int(this._bool_() and right._bool_()))
    def orl(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        return TagInteger(int(this._bool_() and right._bool_()))
    
    def call(self, this: 'TagInstance', args: TagArg, kargs: Kargs, env: 'Enviroment') -> 'TagInstance':
        return make_error("TypeError", f"{this.type} is not callable")
    
    def iter(self, this: 'TagInstance') -> typing.Generator['TagInstance', typing.Any, None]:
        yield make_error("TypeError", f'{this.type} is not iterable')
    
    def repr(self, this: 'TagInstance') -> 'TagInstance':
        return TagString("[Instance:" + this.type.NAME + "]")
    
    def _bool_(self, this: 'TagInstance'):
        return True
    
    def bool(self, this: 'TagInstance') -> 'TagInstance':
        return TagInteger(int(this._bool_()))

class TagNullType(TagBase):
    NAME = "NullType"
    
    def repr(self, this: 'TagInstance'):
        return TagString('null')
    
    def _bool_(self, this: 'TagInstance') -> bool:
        return False

class TagNull(TagInstance):
    
    def __init__(self) -> None:
        super().__init__()
        self.set_type(tag_nulltype)

class TagBaseException(TagBase):
    NAME = "Exception"

class TagException(TagInstance):
    
    def __init__(self, error: str, msg: str) -> None:
        super().__init__()
        self.error: str = error
        self.msg = msg
        self.set_type(tag_exception)

class TagBaseFunction(TagBase):
    NAME = 'function'
    
    def call(self, this: 'TagInstance', args: TagArg, kargs: Kargs, env: 'Enviroment') -> 'TagInstance':
        t = typing.cast(TagFunction, this)
        t.closure.parent = env
        r = t.body(args, kargs, t.closure)
        t.closure.parent = None
        return r

class TagFunction(TagInstance):
    
    def __init__(self, name: str, body: typing.Callable[[TagArg, Kargs, 'Enviroment'], TagInstance]) -> None:
        super().__init__()
        self.name = name
        self.body = body
        self.closure = Enviroment()
        self.set_type(tag_func)

class TagBaseAFunction(TagBase):
    NAME = 'function'
    
    def call(self, this: 'TagInstance', args: TagArg, kargs: Kargs, env: 'Enviroment') -> 'TagInstance':
        t = typing.cast(TagAFunction, this)
        t.closure.parent = env
        r = asyncio.run(t.body(args, kargs, t.closure))
        t.closure.parent = None
        return r

class TagAFunction(TagInstance):
    
    def __init__(self, name: str, body: typing.Callable[[TagArg, Kargs, 'Enviroment'], typing.Coroutine[typing.Any, typing.Any, TagInstance]]) -> None:
        super().__init__()
        self.name = name
        self.body = body
        self.closure = Enviroment()
        self.set_type(tag_Afunc)

class TagBaseInt(TagBase):
    NAME = 'int'
    
    def add(self, this: TagInstance, right: 'TagInstance'):
        t = typing.cast(TagInteger, this)
        if is_number(right):
            return number(t.value + tnumber(right).value)
        return make_error("TypeError", f"{t.type} + {right.type} is not supported")
    def sub(self, this: TagInstance, right: 'TagInstance'):
        t = typing.cast(TagInteger, this)
        if is_number(right):
            return number(t.value - tnumber(right).value)
        return make_error("TypeError", f"{t.type} + {right.type} is not supported")
    def mult(self, this: TagInstance, right: 'TagInstance'):
        t = typing.cast(TagInteger, this)
        if is_number(right):
            return number(t.value * tnumber(right).value)
        return make_error("TypeError", f"{t.type} + {right.type} is not supported")
    def div(self, this: TagInstance, right: 'TagInstance'):
        t = typing.cast(TagInteger, this)
        if is_number(right):
            r = tnumber(right)
            if r.value == 0:
                return make_error("ZeroDivision", f"Zero division")
            return number(t.value / r.value)
        return make_error("TypeError", f"{t.type} + {right.type} is not supported")
    
    def gt(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagInteger, this)
        if is_number(right):
            return TagInteger(int(t.value > tnumber(right).value))
        return TagInteger(0)
    def gteq(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagInteger, this)
        if is_number(right):
            return TagInteger(int(t.value >= tnumber(right).value))
        return TagInteger(0)
    def lt(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagInteger, this)
        if is_number(right):
            return TagInteger(int(t.value < tnumber(right).value))
        return TagInteger(0)
    def lteq(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagInteger, this)
        if is_number(right):
            return TagInteger(int(t.value <= tnumber(right).value))
        return TagInteger(0)
    
    def equal(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        if is_number(right):
            return TagInteger(int(typing.cast(TagInteger, this).value == tnumber(right).value))
        return TagInteger(0)
    
    def pos(self, this: TagInstance):
        return number(+(typing.cast(TagInteger, this)).value)
    def neg(self, this: TagInstance):
        return number(-(typing.cast(TagInteger, this)).value)
    
    def _bool_(self, this: 'TagInstance'):
        return typing.cast(TagInteger, this).value != 0
    
    def repr(self, this: 'TagInstance') -> 'TagInstance':
        return TagString(str(typing.cast(TagInteger, this).value))

class TagBaseFloat(TagBase):
    NAME = 'float'
    
    def add(self, this: TagInstance, right: 'TagInstance'):
        t = typing.cast(TagFloat, this)
        if is_number(right):
            return number(t.value + tnumber(right).value)
        return make_error("TypeError", f"{t.type} + {right.type} is not supported")
    def sub(self, this: TagInstance, right: 'TagInstance'):
        t = typing.cast(TagFloat, this)
        if is_number(right):
            return number(t.value - tnumber(right).value)
        return make_error("TypeError", f"{t.type} + {right.type} is not supported")
    def mult(self, this: TagInstance, right: 'TagInstance'):
        t = typing.cast(TagFloat, this)
        if is_number(right):
            return number(t.value * tnumber(right).value)
        return make_error("TypeError", f"{t.type} + {right.type} is not supported")
    def div(self, this: TagInstance, right: 'TagInstance'):
        t = typing.cast(TagFloat, this)
        if is_number(right):
            r = tnumber(right)
            if r.value == 0:
                return make_error("ZeroDivision", f"Zero division")
            return number(t.value / r.value)
        return make_error("TypeError", f"{t.type} + {right.type} is not supported")
    
    def gt(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagFloat, this)
        if is_number(right):
            return TagInteger(int(t.value > tnumber(right).value))
        return TagInteger(0)
    def gteq(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagFloat, this)
        if is_number(right):
            return TagInteger(int(t.value >= tnumber(right).value))
        return TagInteger(0)
    def lt(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagFloat, this)
        if is_number(right):
            return TagInteger(int(t.value < tnumber(right).value))
        return TagInteger(0)
    def lteq(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagFloat, this)
        if is_number(right):
            return TagInteger(int(t.value <= tnumber(right).value))
        return TagInteger(0)
    
    def equal(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        if is_number(right):
            return TagFloat(int(typing.cast(TagFloat, this).value == tnumber(right).value))
        return TagInteger(0)
    
    def pos(self, this: TagInstance):
        return number(+(typing.cast(TagFloat, this)).value)
    def neg(self, this: TagInstance):
        return number(-(typing.cast(TagFloat, this)).value)
    
    def _bool_(self, this: 'TagInstance'):
        return typing.cast(TagFloat, this).value != 0
    
    def repr(self, this: 'TagInstance') -> 'TagInstance':
        return TagString(str(typing.cast(TagInteger, this).value))

class TagInteger(TagInstance):
    
    def __init__(self, value: int=0) -> None:
        super().__init__()
        self.value = value
        self.set_type(tag_int)
    
    def __repr__(self) -> str:
        return self.value.__repr__()

class TagFloat(TagInstance):
    
    def __init__(self, value: float=0) -> None:
        super().__init__()
        self.value = value
        self.set_type(tag_float)
    
    def __repr__(self) -> str:
        return self.value.__repr__()


class TagBaseString(TagBase):
    NAME = 'string'
    
    def add(self, this: TagInstance, right: 'TagInstance') -> 'TagInstance':
        if right.istype(TagBaseString):
            return TagString(typing.cast(TagString, this).value + typing.cast(TagString, right).value)
        return make_error("TypeError", f"string cannot concatenate with {right.type}")
    
    def mult(self, this: TagInstance, right: 'TagInstance') -> 'TagInstance':
        if right.istype(TagBaseInt):
            return TagString(typing.cast(TagString, this).value * typing.cast(TagInteger, right).value)
        return make_error("TypeError", f"cannot multiply string with {right.type}, must integer")
    
    def equal(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        if right.istype(TagBaseString):
            return TagInteger(int(typing.cast(TagString, this).value == typing.cast(TagString, right).value))
        return TagInteger(0)
    
    def iter(self, this: 'TagInstance') -> typing.Generator['TagInstance', typing.Any, None]:
        for char in typing.cast(TagString, this).value:
            yield TagString(char)
    
    def _bool_(self, this: 'TagInstance'):
        return bool(typing.cast(TagString, this).value)
    
    def repr(self, this: TagInstance):
        return TagString(typing.cast(TagString, this).value.__repr__())

class TagString(TagInstance):
    
    def __init__(self, value: str | list[str] = '') -> None:
        super().__init__()
        if isinstance(value, list):
            self.value = ''.join(value)
        else:
            self.value = value
        self.set_type(tag_str)
        
        add_method(self, 'lower', _str_lower)
        add_method(self, 'upper', _str_upper)
        add_method(self, 'fmt', _str_fmt)
        add_method(self, 'index', _str_index)
    
    def __repr__(self) -> str:
        return self.value

class TagBaseArray(TagBase):
    NAME = 'list'
    
    def add(self, this: TagInstance, right: 'TagInstance') -> 'TagInstance':
        if right.istype(TagBaseArray):
            return TagArray(typing.cast(TagArray, this).value + typing.cast(TagArray, right).value)
        return make_error("TypeError", f"list cannot concatenate with {right.type}")
    
    def mult(self, this: TagInstance, right: 'TagInstance') -> 'TagInstance':
        if right.istype(TagBaseInt):
            return TagArray(typing.cast(TagArray, this).value * typing.cast(TagInteger, right).value)
        return make_error("TypeError", f"cannot multiply list with {right.type}, must integer")
    
    def equal(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        if right.istype(TagBaseArray):
            return TagInteger(int(typing.cast(TagArray, this).value == typing.cast(TagArray, right).value))
        return TagInteger(0)
    
    def iter(self, this: 'TagInstance') -> typing.Generator['TagInstance', typing.Any, None]:
        yield from typing.cast(TagArray, this).value
    
    def _bool_(self, this: 'TagInstance'):
        return bool(typing.cast(TagArray, this).value)
    
    def repr(self, this: TagInstance) -> 'TagInstance':
        return TagString(typing.cast(TagString, this).value.__repr__())

class TagArray(TagInstance):
    
    def __init__(self, value: list[TagInstance]) -> None:
        super().__init__()
        self.value = value
        self.set_type(tag_array)
        
        add_method(self, 'index', _list_index)
        add_method(self, 'contain', _list_contain)
        add_method(self, 'push', _list_push)
        add_method(self, 'remove', _list_remove)
        add_method(self, 'pop', _list_pop)

class TagBaseType(TagBase):
    NAME = 'Type'
    
    def call(self, this: 'TagInstance', args: TagArg, kargs: Kargs, env: 'Enviroment') -> 'TagInstance':
        t = typing.cast(TagType, this)
        o = TagObject(t, env)
        r = o.field['init'].call(args, kargs, o.env)
        if r.istype(TagBaseException):
            return r
        return o

class TagType(TagInstance):
    
    def __init__(self, name: str, methods: dict[str, typing.Callable[[TagArg, Kargs, Enviroment], TagInstance]]) -> None:
        super().__init__()
        self.name = name
        self.methods = methods
        self.set_type(tag_type)
    
    def __repr__(self) -> str:
        return self.name
    
    def method(self, name: str):
        def _(f: typing.Callable[[TagArg, Kargs, Enviroment], TagInstance]):
            self.methods[name] = f
        return _

class TagBaseObject(TagBase):
    NAME = 'Object'
    
    def add(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'add' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.add is not defined')

    def sub(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'sub' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.sub is not defined')

    def mult(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'mult' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.mult is not defined')

    def div(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'div' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.div is not defined')

    def gt(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'gt' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.gt is not defined')

    def gteq(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'gteq' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.gteq is not defined')

    def lt(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'lt' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.lt is not defined')

    def lteq(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'lteq' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.lteq is not defined')

    def equal(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'equal' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.equal is not defined')

    def nequal(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'nequal' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.nequal is not defined')

    def andl(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'andl' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.andl is not defined')

    def orl(self, this: 'TagInstance', right: 'TagInstance') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'orl' in t.field:
            return t.field['add'].call([right], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.orl is not defined')
    
    def pos(self, this: 'TagInstance'):
        t = typing.cast(TagObject, this)
        if 'pos' in t.field:
            return t.field['positive'].call([], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.positive is not defined')
    
    def neg(self, this: 'TagInstance'):
        t = typing.cast(TagObject, this)
        if 'neg' in t.field:
            return t.field['negate'].call([], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.negate is not defined')
    
    def notb(self, this: 'TagInstance'):
        t = typing.cast(TagObject, this)
        if 'not' in t.field:
            return t.field['notb'].call([], {}, t.env)
        return make_error('TypeError', f'{t.obj_type}.notb is not defined')
    
    def call(self, this: 'TagInstance', args: TagArg, kargs: Kargs, env: 'Enviroment') -> 'TagInstance':
        t = typing.cast(TagObject, this)
        if 'call' in t.field:
            return t.field['call'].call([], {}, t.env)
        return make_error('TypeError', f'{t.obj_type} is not callable')
    
    def repr(self, this: 'TagInstance'):
        t = typing.cast(TagObject, this)
        return t.field['repr'].call([], {}, t.env)

class TagObject(TagInstance):
    
    def __init__(self, type: TagType, env: Enviroment) -> None:
        super().__init__()
        self.obj_type = type
        self.env = Enviroment(env)
        self.env.set('this', self)
        self.sfield: dict[str, TagInstance] = {}
        self.set_type(tag_object)
        
        add_method(self, 'init', _empty_method)
        add_method(self, 'repr', _obj_repr)
        
        for n, m in self.obj_type.methods.items():
            add_method(self, n, m)

def tnumber(v: TagInstance):
    if v.istype(TagBaseInt):
        return typing.cast(TagInteger, v)
    elif v.istype(TagBaseFloat):
        return typing.cast(TagFloat, v)
    raise Exception(f"tnumber got non-number, {v.type}")

def number(v: int | float):
    if isinstance(v, int):
        return TagInteger(v)
    return TagFloat(v)

def is_number(v: TagInstance):
    return v.istype(TagBaseInt) or v.istype(TagBaseFloat)

tag_exception = TagBaseException()
tag_int = TagBaseInt()
tag_float = TagBaseFloat()
tag_str = TagBaseString()
tag_func = TagBaseFunction()
tag_Afunc = TagBaseAFunction()
tag_nulltype = TagNullType()
tag_array = TagBaseArray()
tag_type = TagBaseType()
tag_object = TagBaseObject()

tag_null = TagNull()

def make_error(err: str, msg: str):
    return TagException(err, msg)

def argerror(where: str, need: int, got: list[typing.Any]):
    return make_error("TypeError", f"{where} required {need} argument, got {len(got)}")

def add_method(t: TagInstance, name: str, func: typing.Callable[[TagArg, Kargs, 'Enviroment'], TagInstance]):
    m = TagFunction(name, func)
    m.closure.set('this', t)
    t.field[name] = m

def add_Amethod(t: TagInstance, name: str, func: typing.Callable[[TagArg, Kargs, 'Enviroment'], typing.Coroutine[typing.Any, typing.Any, TagInstance]]):
    m = TagAFunction(name, func)
    m.closure.set('this', t)
    t.field[name] = m

def _str_lower(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = typing.cast(TagString, env.get('this'))
    return TagString(this.value.lower())

def _str_upper(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = typing.cast(TagString, env.get('this'))
    return TagString(this.value.upper())

def _str_fmt(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = typing.cast(TagString, env.get('this'))
    
    s = this.value
    for i, a in enumerate(args):
        _a = a.__repr__()
        s = s.replace('{}', _a, 1)
        if '{'+str(i)+'}' in _a:
            s = s.replace('{'+str(i)+'}', _a)
    
    for n, v in kwargs.items():
        s = s.replace('{'+n+'}', v.__repr__())
    
    return TagString(s)

def _list_index(args: TagArg, kwargs: Kargs, env: Enviroment):
    if len(args) != 1:
        return argerror('list.index', 1, args)
    i = args[0]
    
    if i.istype(TagBaseInt):
        try:
            return typing.cast(TagArray, env.get('this')).value[typing.cast(TagInteger, i).value]
        except IndexError:
            return make_error('IndexError', 'list out of bound')
    return make_error('TypeError', f'list indexing only accept integer not {i.type}')

def _list_contain(args: TagArg, kwargs: Kargs, env: Enviroment):
    if len(args) != 1:
        return argerror('list.contain', 1, args)
    i = args[0]

    for o in env.get('this').iter():
        if i.equal(o)._bool_():
            return TagInteger(1)
    return TagInteger(0)

def _list_remove(args: TagArg, kwargs: Kargs, env: Enviroment):
    if len(args) != 1:
        return argerror('list.remove', 1, args)
    i = args[0]

    this = typing.cast(TagArray, env.get('this'))
    
    for c, o in enumerate(this.iter()):
        if i.equal(o)._bool_():
            this.value.pop(c)
    
    return tag_null

def _list_push(args: TagArg, kwargs: Kargs, env: Enviroment):
    if len(args) != 1:
        return argerror('list.append', 1, args)
    i = args[0]

    this = typing.cast(TagArray, env.get('this'))
    
    this.value.append(i)
    
    return tag_null

def _list_pop(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = typing.cast(TagArray, env.get('this'))
    
    if len(args) != 1:
        try:
            this.value.pop()
        except IndexError:
            return make_error('IndexError', 'list out of bound')
    
    i = args[0]
    
    if not i.istype(TagBaseInt):
        return make_error('TypeError', f'list.pop required integer not {i.type}')

    try:
        this.value.pop(typing.cast(TagInteger, i).value)
    except IndexError:
        return make_error('IndexError', 'list out of bound')
    
    return tag_null

def _str_index(args: TagArg, kwargs: Kargs, env: Enviroment):
    if len(args) != 1:
        return argerror('str.index', 1, args)
    i = args[0]
    
    if i.istype(TagBaseInt):
        try:
            return TagString(typing.cast(TagString, env.get('this')).value[typing.cast(TagInteger, i).value])
        except IndexError:
            return make_error('IndexError', 'string out of bound')
    return make_error('TypeError', f'string indexing only accept integer not {i.type}')

def _empty_method(args: TagArg, kwargs: Kargs, env: Enviroment):
    return tag_null

def _obj_repr(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = typing.cast(TagObject, env.get('this'))
    return TagString(f'[Instance:{this.obj_type.name}]')

def get_this(env: Enviroment):
    return typing.cast(TagObject, env.get('this'))

def icopy(i: TagInstance, *args: typing.Any):
    s = i.__class__(*args)
    s.field = {**i.field.copy(), **s.field}
    return s
from .tag_builtin import *
from typing import cast

def tstring(t: TagInstance):
    return typing.cast(TagString, t).value

def tarray(t: TagInstance):
    return typing.cast(TagArray, t).value


def print_(args: TagArg, kwargs: Kargs, env: Enviroment):
    sep = kwargs.get('sep')
    if sep is None:
        _sep = ' '
    elif sep.istype(TagBaseString):
        _sep = typing.cast(TagString, sep).value
    else:
        _sep = ' '
    
    s = ''
    for arg in args:
        r = arg.__repr__()
        if isinstance(r, str):
            s += r + _sep
        else:
            return make_error('TypeError', f'{arg.type}.repr did not return string')
    print(s)
    return tag_null

Table = TagType('Table', {})
_LOCKED_METHOD_TABLE = ('init','get','set')

@Table.method('init')
def table_init(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = get_this(env)
    
    for n, k in kwargs.items():
        if n in _LOCKED_METHOD_TABLE:
            return make_error('TableError', f'{n} is not allowed name for table item')
        this.field[n] = k
    
    return tag_null

@Table.method('get')
def table_get(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = get_this(env)
    
    if len(args) != 1:
        return argerror('Table.get', 1, args)
    
    a = args[0]
    if a.istype(TagBaseString):
        return this.field[typing.cast(TagString, a).value]
    return make_error('TypeError', f'Table.get required string not {a.type}')

@Table.method('set')
def table_set(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = get_this(env)
    
    if len(args) != 2:
        return argerror('Table.set', 2, args)
    
    n = args[0]
    v = args[1]
    
    if n.istype(TagBaseString):
        this.field[typing.cast(TagString, n).value] = v
        return this
    return make_error('TypeError', f'Table.set first argument required string not {n.type}')

@Table.method('repr')
def table_repr(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = get_this(env)
    return TagString(this.field.__repr__())


def slice_(args: TagArg, kwargs: Kargs, env: Enviroment):
    if len(args) != 1:
        return argerror('slice', 1, args)
    v = args[0]
    
    s, e = kwargs.get('s') or tag_null, kwargs.get('e') or tag_null
    
    if s.istype(TagBaseInt):
        _s = typing.cast(TagInteger, s).value
    else:
        _s = None
    if e.istype(TagBaseInt):
        _e = typing.cast(TagInteger, e).value
    else:
        _e = None
    
    g = list(v.iter())
    if g:
        if g[0].istype(TagBaseException):
            return g
    
    try:
        s_ = g[_s:_e]
    except IndexError:
        return make_error("IndexError", f"{v.type} out of bound")
    
    if v.istype(TagBaseString):
        return TagString([typing.cast(TagString, x).value for x in s_])
    return TagArray(s_)

def expect(where: str, args: list[type], kwargs: dict[str, type], a: TagArg, k: Kargs):
    if len(a) != len(args):
        return False, argerror(where, len(args), a)
    
    _i = 1
    for arg, argt in zip(a, args):
        if not arg.istype(argt):
            return False, make_error('TypeError', f'{where} argument {_i} expected to be {argt} but got {arg}')
        _i += 1
    
    for n, v in k.items():
        if n in kwargs:
            if not v.istype(kwargs[n]):
                return False, make_error('TypeError', f'{where} argument \'{n}\' expected to be {kwargs[n]} but got {v.type}')
    
    for n in kwargs.keys():
        if n not in k:
            return False, make_error('TypeError', f'{where} required \'{n}\' argument')
    
    return True, None
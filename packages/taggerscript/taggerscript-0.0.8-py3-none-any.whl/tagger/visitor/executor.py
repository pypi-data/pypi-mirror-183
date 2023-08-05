from core.node import *
from core.klass import TagInstance, Enviroment
from .tag_builtin import *

import typing

def _extend(t: type):
    def _(f):
        setattr(t, 'execute', f)
    return _


def evaluate(n: Node, env: Enviroment):
    x = n.execute(env)
    if env.error:
        return tag_null
    if x.istype(TagBaseException):
        y = typing.cast(TagException, x)
        env.throw(y.error, y.msg, n.l, n.c)
        return tag_null
    return x


@_extend(NLiteral)
def _nliteral(node: NLiteral, env: Enviroment):
    if isinstance(node.value, str):
        return TagString(node.value)
    if isinstance(node.value, int):
        return TagInteger(node.value)
    else:
        return TagFloat(node.value)

@_extend(NArithmetic)
def _narith(node: NArithmetic, env: Enviroment):
    l, r = evaluate(node.left, env), evaluate(node.right, env)
    if env.error:
        return tag_null
    
    if node.op == '+':
        return l.add(r)
    elif node.op == '-':
        return l.sub(r)
    elif node.op == '*':
        return l.mult(r)
    elif node.op == '/':
        return l.div(r)

@_extend(NUnary)
def _nunary(node: NUnary, env: Enviroment):
    v = evaluate(node.value, env)
    if env.error:
        return tag_null
    
    if node.op == '+':
        return v.pos()
    elif node.op == '-':
        return v.neg()
    else:
        return v.notb()

@_extend(NSetVar)
def _nsetvar(node: NSetVar, env: Enviroment):
    v = evaluate(node.value, env)
    if env.error:
        return tag_null
    
    env.set(node.name, v)
    return tag_null

@_extend(NCmp)
def _ncmp(node: NCmp, env: Enviroment):
    l, r = evaluate(node.left, env), evaluate(node.right, env)
    if env.error:
        return tag_null
    
    if node.op == '>':
        return l.gt(r)
    elif node.op == '<':
        return l.lt(r)
    elif node.op == '>=':
        return l.gteq(r)
    elif node.op == '<=':
        return l.lteq(r)
    elif node.op == '==':
        return l.equal(r)
    elif node.op == '!=':
        return l.nequal(r)
    elif node.op == 'and':
        return l.andl(r)
    elif node.op == 'or':
        return l.orl(r)

@_extend(NGetVar)
def _ngetvar(node: NGetVar, env: Enviroment):
    v = env.get(node.name)
    if v:
        return v
    env.throw("NameError", f"No {node.name} found in current scope", node.l, node.c)
    return tag_null

@_extend(NDo)
def _ndo(node: NDo, env: Enviroment):
    r: TagInstance = tag_null
    for n in node.tree:
        r = evaluate(n, env)
    return r

@_extend(NDot)
def _ndot(node: NDot, env: Enviroment):
    v = evaluate(node.left, env)
    if env.error:
        return tag_null
    
    x = v.field.get(node.right)
    if x:
        return x
    env.throw('AttributeError', f'No attribute {node.right} found in {v.type}', node.l, node.c)
    return tag_null

@_extend(NFieldSet)
def _nfieldset(node: NFieldSet, env: Enviroment):
    v = evaluate(node.value, env)
    if env.error:
        return tag_null
    
    o = env.get(node.origin)
    if o is None:
        env.throw("NameError", f"No {node.origin} found in current scope", node.l, node.c)
        return tag_null
    
    i = ''
    for n in node.field:
        _o = o
        o = _o.field.get(n)
        if o is None:
            env.throw("AttributeError", f"No attribute {n} found in {v.type}", node.l, node.c)
            return tag_null
        i = n
    
    _o.field[i] = v
    return tag_null

@_extend(NCall)
def _ncall(node: NCall, env: Enviroment):
    c = evaluate(node.caller, env)
    if env.error:
        return
    
    a: TagArg = []
    for arg in node.args:
        a.append(evaluate(arg, env))
    
    ka: Kargs = {}
    for n, arg in node.argk.items():
        ka[n] = evaluate(arg, env)
    
    if env.error:
        return tag_null
    
    return c.call(a, ka, env)

@_extend(NArray)
def _narray(node: NArray, env: Enviroment):
    r = TagArray([])
    for n in node.value:
        a = evaluate(n, env)
        r.value.append(a)
    return r

@_extend(NIfElse)
def _nif(node: NIfElse, env: Enviroment):
    cond = evaluate(node.cond, env)
    if env.error:
        return tag_null
    
    if cond.bool():
        return evaluate(node.body, env)
    else:
        if node.elif_:
            for i in node.elif_:
                c = evaluate(i.cond, env)
                if c.bool():
                    return evaluate(i.body, env)
        if node.else_:
            return evaluate(node.else_.body, env)
    return tag_null

@_extend(NWhile)
def _nwhile(node: NWhile, env: Enviroment):
    r: TagInstance = tag_null
    while evaluate(node.cond, env).bool():
        r = evaluate(node.body, env)
    if env.error:
        return tag_null
    return r

@_extend(NFor)
def _nfor(node: NFor, env: Enviroment):
    v = evaluate(node.value, env)
    if env.error:
        return
    
    s = Enviroment(env)
    for i in v.iter():
        s.set(node.name, i)
        evaluate(node.body, s)
        if s.error:
            return tag_null
    env.error += s.error
    return tag_null
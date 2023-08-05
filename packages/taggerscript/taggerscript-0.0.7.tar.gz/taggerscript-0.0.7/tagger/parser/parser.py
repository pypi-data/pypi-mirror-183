from lark import Lark, Transformer, Token, Tree
from lark.exceptions import UnexpectedCharacters, UnexpectedEOF, UnexpectedToken
from core.node import *
from core.error import Error

tparser = Lark(open('parser/tagger.lark'))

def tparse(text: str):
    try:
        return tparser.parse(text)
    except UnexpectedCharacters as e:
        return Error('SyntaxError', 'Unexpected character', e.line, e.column)
    except UnexpectedToken as e:
        return Error('SyntaxError', 'Invalid Syntax', e.line, e.column)
    except UnexpectedEOF:
        l = text.splitlines()
        return Error('SyntaxError', 'Unexpted End of line', len(l), len(l[-1]))

Terminal = tuple[Token]
BinOp = tuple[Node, Token, Node]

class TagTransformer(Transformer):
    
    def start(self, t):
        return t

    def integer(self, t: Terminal):
        (v,) = t
        return NLiteral(v.line, v.column, int(v)) # type: ignore
    
    def float_(self, t: Terminal):
        (v,) = t
        return NLiteral(v.line, v.column, float(v)) # type: ignore
    
    def string(self, t: Terminal):
        (v,) = t
        a = str(v[1:-1])
        _a = ''
        _p = ''
        for c in a:
            if _p == '\\':
                if c == 'n':
                    _a += '\n'
                elif c == 't':
                    _a += '\t'
                elif c == 'r':
                    _a += '\r'
                else:
                    _a += c
                _p = c
                continue
            _p = c
            if c != '\\':
                _a += c
        return NLiteral(v.line, v.column, _a) # type: ignore
    
    def array(self, t):
        b, v = t[0], t[1:]
        return NArray(b.line, b.column, v or []) # type: ignore
    
    def arith(self, t: BinOp):
        l, o, r = t
        return NArithmetic(o.line, o.column, l, o, r) # type: ignore
    
    def unary(self, t: tuple[Token, Node]):
        o, v = t
        return NUnary(o.line, o.column, o, v) # type: ignore
    
    def cmp(self, t: BinOp):
        l, o, r = t
        return NCmp(o.line, o.column, l, o, r) # type: ignore
    
    def tagdo(self, t: list[Node]):
        d, a = t[0], t[1:]
        return NDo(d.line, d.column, a) # type: ignore
    
    def tagvar(self, t: tuple[Token, Node]):
        n, v = t
        return NSetVar(n.line, n.column, str(n), v) # type: ignore
    
    def getvar(self, t: Terminal):
        (n,) = t
        return NGetVar(n.line, n.column, str(n)) # type: ignore
    
    def dot(self, t: BinOp):
        l, o, r = t
        return NDot(o.line, o.column, l, r) # type: ignore
    
    def keyarg(self, t: tuple[Token, Node]):
        return (str(t[0]), t[1])
    
    def call(self, t: tuple[Node, list[Node | tuple[str, Node]]]):
        caller, arg = t
        r = NCall(caller.l, caller.c, caller, [], {}) # type: ignore
        for a in arg.children: # type: ignore
            if isinstance(a, Node):
                r.args.append(a)
            else:
                r.argk[a[0]] = a[1]
        return r
    
    def fieldset(self, t: tuple[list[Token], Node]):
        n, v = t[0].children, t[1] # type: ignore
        return NFieldSet(n[0].line, n[0].column, n[0], n[1:], v) # type: ignore
    
    # syntantic sugar
    def indexing(self, t: tuple[Node, Token, NLiteral]):
        n, o, i = t
        return NCall(o.line, o.column, NDot(o.line, o.column, n, 'index'), [i], {}) # type: ignore
    
    def tagelse(self, t: tuple[Token, Node]):
        s, b = t
        if s is None:
            return None
        return NElse(s.line, s.column, b)
    
    def tagelif(self, t: tuple[Token, Node, Node]):
        s, c, b = t
        if s is None:
            return None
        return NElif(s.line, s.column, c, b)
    
    def tagif(self, t: list[Token | Tree | Node]): # type: ignore
        stmt, cond, body = t[:3]
        elif_ = t[3:-1]
        else_ = t[-1]
        
        if None in elif_:
            elif_ = []
        
        return NIfElse(stmt.line, stmt.column, cond, body, elif_, else_) # type: ignore
    
    def tagwhile(self, t: tuple[Token, Node, Node]):
        s, c, b = t
        return NWhile(s.line, s.column, c, b)
    
    def tagfor(self, t: tuple[Token, Token, Node, Node]):
        s, n, v, b = t
        return NFor(s.line, s.column, str(n), v, b)
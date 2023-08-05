import random

from visitor.obj_builtin import  *

def randint(args: TagArg, kargs: Kargs, env: Enviroment):
    success, er = expect('randint', [TagBaseInt, TagBaseInt], {}, args, kargs)
    if not success:
        return er
    
    a_, b_ = cast(TagInteger, args[0]).value, cast(TagInteger, args[1]).value
    
    return TagInteger(random.randint(a_, b_))

def randchoice(args: TagArg, kargs: Kargs, env: Enviroment):
    success, er = expect('randchoice', [TagArray], {}, args, kargs)
    if not success:
        return er
    
    a = cast(TagArray, args[0])
    
    if len(a.value) == 0:
        return tag_null
    
    return random.choice(a.value)
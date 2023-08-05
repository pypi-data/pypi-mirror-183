import discord
from discord.ext import commands

from visitor.obj_builtin import *

class UserBase(TagBase):
    NAME = 'User'

class User(TagInstance):
    
    def __init__(self, user: discord.User | discord.Member) -> None:
        super().__init__()
        self.user = user
        self.set_type(user_)
        
        self.field['name'] = TagString(user.name)
        self.field['id'] = TagInteger(user.id)
        self.field['avatar'] = TagString(user.display_avatar.url)
        self.field['bot'] = TagInteger(int(user.bot))

class MessageBase(TagBase):
    NAME = 'Message'

class Message(TagInstance):
    
    def __init__(self, msg: discord.Message) -> None:
        super().__init__()
        self.msg = msg
        self.set_type(message)
        
        self.field['author'] = User(self.msg.author)
        self.field['id'] = TagInteger(self.msg.id)
        self.field['content'] = TagString(self.msg.content)

class ContextTagBase(TagBase):
    NAME = 'MessageTag'

class ContextTag(TagInstance):
    
    def __init__(self, bot: commands.Bot, ctx: commands.Context) -> None:
        super().__init__()
        self.msg = ctx.message
        self.bot = bot
        self.ctx = ctx
        self.set_type(messagetag)
        
        self.field['user'] = User(self.ctx.message.author)
        self.field['message'] = Message(ctx.message)
        
        add_Amethod(self, 'set', _ctx_set)
        add_Amethod(self, 'add', _ctx_add)
        add_Amethod(self, 'wait_for_react', _ctx_waitfor_reaction)
        add_Amethod(self, 'wait_for_reply', _ctx_waitfor_reply)

messagetag = ContextTagBase()
user_ = UserBase()
message = MessageBase()

async def get_this_msg(env: Enviroment) -> ContextTag:
    return typing.cast(ContextTag, env.get('this'))

async def _ctx_set(args: TagArg, kwargs: Kargs, env: Enviroment) -> TagInstance:
    this = await get_this_msg(env)
    
    try:
        await this.msg.edit(content=(' '.join([arg.__repr__() for arg in args] or ['``````'])))
    except Exception as e:
        return make_error('DisTagError', e.args[0].__str__())
    
    return tag_null

async def _ctx_add(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = await get_this_msg(env)
    
    try:
        await this.msg.edit(content=(this.msg.content + (' '.join([arg.__repr__() for arg in args] or ['']))))
    except Exception as e:
        return make_error('DisTagError', e.args[0].__str__())
    
    return tag_null

async def _ctx_waitfor_reaction(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = await get_this_msg(env)
    
    success, er = expect('MessageTag.wait_for_react', [TagBaseString], {}, args, kwargs)
    if not success:
        return er
    
    t = tstring(args[0])
    
    r: discord.Reaction | None = this.bot.wait_for('reaction_add', check=lambda r: r.emoji.name == t, timeout=100)
    
    if r is None:
        return tag_null
    
    v: list[TagInstance] = []
    async for u in r.users():
        v.append(User(u))
    return TagArray(v)

async def _ctx_waitfor_reply(args: TagArg, kwargs: Kargs, env: Enviroment):
    this = await get_this_msg(env)
    
    r: discord.Message = this.bot.wait_for('message', check=lambda m: this.bot in m.mentions, timeout=100)
    
    if r is None:
        return tag_null
    
    return Message(r)
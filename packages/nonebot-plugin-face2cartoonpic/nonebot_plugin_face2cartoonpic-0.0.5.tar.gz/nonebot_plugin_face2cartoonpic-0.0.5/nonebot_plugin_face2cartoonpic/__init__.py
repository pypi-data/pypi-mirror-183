from pathlib import Path

import nonebot
from nonebot.typing import T_State
from nonebot import get_driver,on_command,on_regex
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message, MessageSegment,MessageEvent
from nonebot.adapters.onebot.v11.helpers import extract_image_urls
from nonebot.params import Arg
from nonebot.log import logger

from .config import Config
from .limiter import limiter
from .tencentapi import get_pic

fc = on_regex('人像变换', priority=5, block=True)


@fc.handle()
async def image2comic(event: MessageEvent, matcher: Matcher):
    message = reply.message if (reply := event.reply) else event.message
    if imgs := message["image"]:
        matcher.set_arg("imgs", imgs)
   
@fc.got("imgs", prompt="请发送用于启动的原图")
async def get_image(state: T_State, imgs: Message = Arg()):
    urls = extract_image_urls(imgs)
    if not urls:
        await fc.finish("没有找到图片,请重新启动并在启动语句后添加图片")
        
    state["urls"] = urls




@fc.handle()
async def _handle(matcher: Matcher,event: MessageEvent,state: T_State):
    
    user_id = event.user_id
    if not limiter.check(user_id):
        left_time = limiter.left_time(user_id)
        await matcher.finish(f'我知道你急了.但是你先别急,cd还有{left_time}秒')
        return 
    url_input = state["urls"][0]
    limiter.start_cd(user_id)
    try:
        msg_raw = await get_pic(url_input)
    except Exception as e:
        logger.opt(exception=e).error("画图失败")
        await fc.finish("寄，画图失败了", reply_message=True)    
    url = msg_raw
    await fc.send(url)
    await fc.finish(MessageSegment.image(file=url, cache=False), at_sender=True)
    
 



_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").
    resolve()))


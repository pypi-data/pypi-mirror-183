from nonebot.plugin.on import on_regex
from nonebot.adapters.onebot.v11 import (
    Bot,
    MessageEvent,
    PrivateMessageEvent,
    MessageSegment,
    Message
    )

import re
import random
import nonebot
import requests
import unicodedata

try:
    import ujson as json
except ModuleNotFoundError:
    import json

Bot_NICKNAME: str = list(nonebot.get_driver().config.nickname)[0]

# anosu

anosu = on_regex("^(我?要|来).*[张份].+$", priority = 50, block = True)

@anosu.handle()
async def _(bot: Bot, event: MessageEvent):
    msg = ""
    cmd = event.get_plaintext()
    N = re.sub(r'^我?要|^来|[张份].+$', '', cmd)
    N = N if N else 1

    try:
        N = int(N)
    except ValueError:
        try:
            N = int(unicodedata.numeric(N))
        except (TypeError, ValueError):
            N = 0

    tag = re.sub(r'^我?要|^来|.*[张份]', '', cmd)
    tag = tag [:-2]if (tag.endswith("涩图") or tag.endswith("色图")) else tag

    if tag.startswith("r18"):
        tag = tag [3:]
        r18 = 1
    else:
        r18 = 0

    if 1 <= N <= 10:
        msg += f"{Bot_NICKNAME}为你准备了{N}张随机{tag}色图。"
    elif N > 10:
        msg += f"{Bot_NICKNAME}为你的身体着想，为你准备了一张随机{tag}色图。"
        N = 1
    else:
        msg += f"没有听懂呢，不过{Bot_NICKNAME}送你一张随机{tag}色图。"
        N = 1

    resp = requests.get(f"https://image.anosu.top/pixiv/json?num={N}&r18={r18}&keyword={tag}")
    if resp.status_code == 200:
        resp = resp.text
        resp = ''.join(x for x in resp if x.isprintable())
        anosu_list = json.loads(resp)
    else:
        anosu_list = None

    if not anosu_list:
        if anosu_list == []:
            await anosu.send(f"没有找到【{tag}】")
        else:
            await anosu.send("连接出错了...")

    elif N <= 3:
        image = Message()
        for i in range(N):
            image +=  MessageSegment.image(file = anosu_list[i]["url"])
        await anosu.send(Message(msg) + image, at_sender = True)
    else:
        await anosu.send(msg, at_sender = True)
        msg_list =[]
        for i in range(N):
            msg_list.append(
                {
                    "type": "node",
                    "data": {
                        "name": Bot_NICKNAME,
                        "uin": event.self_id,
                        "content": MessageSegment.image(file = anosu_list[i]["url"])
                        }
                    }
                )
        await bot.send_private_forward_msg(user_id = event.user_id, messages = msg_list)
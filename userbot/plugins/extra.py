import asyncio, subprocess
import time, re, io
from userbot import bot, BOTLOG, BOTLOG_CHATID, CMD_HELP
from telethon import events, functions, types
from telethon.events import StopPropagation
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.channels import LeaveChannelRequest, CreateChannelRequest, DeleteMessagesRequest
from collections import deque
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.utils import admin_cmd

@borg.on(admin_cmd("leave"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`நான் இந்த குழுவை விட்டு வெளியேறுகிறேன்!🚶 🚶 🚶`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`இது ஒரு குழு அல்ல`')

@borg.on(admin_cmd("hm"))
#@register(outgoing=True, pattern="^;__;$")
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)

@borg.on(admin_cmd("oof"))
#@register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)

@borg.on(admin_cmd("cry"))
#@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")

@borg.on(admin_cmd("fp"))
#@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")

@borg.on(admin_cmd("moon"))
#@register(outgoing=True, pattern="^.mmoon$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd("source"))
#@register(outgoing=True, pattern="^.source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("github.com/TamilBots/TamilBot")
        
@borg.on(admin_cmd("readme"))
#@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/TamilBots/TamilBot/blob/master/README.md")



@borg.on(admin_cmd("heart"))		
#@register(outgoing=True, pattern="^.heart$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("❤️🧡💛💚💙💜🖤"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd("king"))
#@register(outgoing=True, pattern="^.king$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("👉🤴🏻👉🙂👉😎"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd(pattern=r"hack"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "hack":

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        if idd==813878981:
            await event.edit("This is My Master\nI can't hack my master's Account\n**How dare you trying to hack my master's account AssKisser!**\n\n__Your account has been hacked! Pay 69$ to my master__ [FridayOT](t.me/fridayOT) __to release your account__😏")
        else:
            await event.edit("Hacking..")
            animation_chars = [
        
            "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
            "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package",
            "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)",    
            "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e",
            "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b",
            "`Hacking... 84%\n█████████████████████▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**",
            "`Hacking... 100%\n█████████HACKED███████████ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.66 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**\n\n\n🔹Output: Generating.....",
            "`Targeted Account Hacked...\n\nPay 999999999$ To My Boss Remove this hack....`\n\nTERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked this Account From Telegram Database**\n\n\n🔹**Output:** Successful"

            ]

            for i in animation_ttl:

                await asyncio.sleep(animation_interval)

                await event.edit(animation_chars[i % 11])
    else:
        await event.edit("No User is Defined\n are u dumb\n reply to a user.")

		
CMD_HELP.update(
    {
        "Extra":

        """╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.leave`
 ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Leave a Chat__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.hm`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾   __You try it!__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.cry`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Send face palm emoji.__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.moon`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ __Bot will send a cool moon animation.__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.clock`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ __Bot will send a cool clock animation.__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.readme`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ __Reedme.__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.source`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ __Gives the source of your userbot__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.myusernames`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __List of Usernames owned by you.__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.oof`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Same as ;__; but ooof__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.earth`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Sends Earth animation__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.hack`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __hack targeted users database__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.heart`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Try and you'll get your emotions back__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.king`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Be The Real King__
"""
    }
)

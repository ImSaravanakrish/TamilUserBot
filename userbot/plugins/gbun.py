# This is a troll indeed ffs *facepalm*
import asyncio
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd


@borg.on(admin_cmd("gbun"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n`"
    no_reason = "𝗥𝗲𝗮𝘀𝗼𝗻 : __Not given __"
    await event.edit("𝐔𝐬𝐞𝐫 𝐆𝐛𝐚𝐧𝐧𝐢𝐧𝐠 𝐒𝐨𝐨𝐧... ❗️⚜️☠️")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1492186775 or idd == 1169076058 :
            await reply_message.reply("`ஒரு நொடி காத்திரு, இது என் எஜமான்!`\n**என் மாஸ்டர்-யை தடை செய்ய நீங்கள் அச்சுறுத்துகிறீர்கள்!**\n\n__உங்கள் Account ஹேக் செய்யப்பட்டுள்ளது! என் எஜமானருக்கு 69$ செலுத்துங்கள்__ [Vetri](tg://user?id=1492186775) __உங்கள் Account-யை வெளியிட__😏")
        else:
            jnl=("`Warning!! `"
                  "[{}](tg://user?id={})"
                  "` 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n\n`"
                  "**Person's Name: ** __{}__\n"
                  "**ID : ** `{}`\n"
                ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Victim username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Victim username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **"+gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\nReason: Not Given `"
        await event.reply(mention)
    await event.delete()

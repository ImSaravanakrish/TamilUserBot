# by @saravanakrish for @tamiluserbot
# Fully Written by @HeisenbergTheDanger (Keep credits else gay)

import base64
from asyncio import sleep

from telethon.tl.types import InputMediaUploadedPhoto
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot.plugins.sql_helper import broadcast_sql as sql
from userbot.utils import admin_cmd
from userbot.manager.utils import edit_delete, edit_or_reply
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP

parse_pre="html"



@borg.on(admin_cmd(pattern="sendto(?: |$)(.*)", command="sendto"))
async def userbroadcast_send(event):
    if event.fwd_from:
        return
    userinput_str = event.pattern_match.group(1)
    if not userinput_str:
        return await edit_delete(
            event, "To which category should i send this message", parse_mode=parse_pre
        )
    reply = await event.get_reply_message()
    user = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    if not reply:
        return await edit_delete(
            event, "what should i send to to this category ?", parse_mode=parse_pre
        )
    keyword = userinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    group_ = Get(user)
    if no_of_chats == 0:
        return await edit_delete(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    userevent = await edit_or_reply(
        event,
        "sending this message to all groups in the category",
        parse_mode=parse_pre,
    )
    try:
        await event.client(group_)
    except BaseException:
        pass
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.send_message(int(chat), reply)
            i += 1
        except Exception as e:
            LOGS.info(str(e))
        await sleep(0.5)
    resultext = f"`The message was sent to {i} chats out of {no_of_chats} chats in category {keyword}.`"
    await userevent.edit(resultext)
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"A message is sent to {i} chats out of {no_of_chats} chats in category {keyword}",
            parse_mode=parse_pre,
        )


@borg.on(admin_cmd(pattern="fwdto(?: |$)(.*)", command="fwdto"))
async def userbroadcast_send(event):
    if event.fwd_from:
        return
    userinput_str = event.pattern_match.group(1)
    if not userinput_str:
        return await edit_delete(
            event, "To which category should i send this message", parse_mode=parse_pre
        )
    reply = await event.get_reply_message()
    user = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    if not reply:
        return await edit_delete(
            event, "what should i send to to this category ?", parse_mode=parse_pre
        )
    keyword = userinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    group_ = Get(user)
    if no_of_chats == 0:
        return await edit_delete(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    userevent = await edit_or_reply(
        event,
        "sending this message to all groups in the category",
        parse_mode=parse_pre,
    )
    try:
        await event.client(group_)
    except BaseException:
        pass
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.forward_messages(int(chat), reply)
            i += 1
        except Exception as e:
            LOGS.info(str(e))
        await sleep(0.5)
    resultext = f"`The message was sent to {i} chats out of {no_of_chats} chats in category {keyword}.`"
    await catevent.edit(resultext)
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"A message is forwared to {i} chats out of {no_of_chats} chats in category {keyword}",
            parse_mode=parse_pre,
        )


@borg.on(admin_cmd(pattern="addto(?: |$)(.*)", command="addto"))
async def userbroadcast_add(event):
    if event.fwd_from:
        return
    userinput_str = event.pattern_match.group(1)
    if not userinput_str:
        return await edit_delete(
            event, "In which category should i add this chat", parse_mode=parse_pre
        )
    keyword = userinput_str.lower()
    check = sql.is_in_broadcastlist(keyword, event.chat_id)
    if check:
        return await edit_delete(
            event,
            f"This chat is already in this category {keyword}",
            parse_mode=parse_pre,
        )
    sql.add_to_broadcastlist(keyword, event.chat_id)
    await edit_delete(
        event, f"This chat is Now added to category {keyword}", parse_mode=parse_pre
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is added to category {keyword}",
                parse_mode=parse_pre,
            )
        except Exception:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is added to category {keyword}",
                parse_mode=parse_pre,
            )

@borg.on(admin_cmd(pattern="rmfrom(?: |$)(.*)", command="rmfrom"))
async def userbroadcast_remove(event):
    if event.fwd_from:
        return
    userinput_str = event.pattern_match.group(1)
    if not userinput_str:
        return await edit_delete(
            event, "From which category should i remove this chat", parse_mode=parse_pre
        )
    keyword = userinput_str.lower()
    check = sql.is_in_broadcastlist(keyword, event.chat_id)
    if not check:
        return await edit_delete(
            event, f"This chat is not in the category {keyword}", parse_mode=parse_pre
        )
    sql.rm_from_broadcastlist(keyword, event.chat_id)
    await edit_delete(
        event,
        f"This chat is Now removed from the category {keyword}",
        parse_mode=parse_pre,
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is removed from category {keyword}",
                parse_mode=parse_pre,
            )
        except Exception:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is removed from category {keyword}",
                parse_mode=parse_pre,
            )


@borg.on(admin_cmd(pattern="list(?: |$)(.*)", command="list"))
async def userbroadcast_list(event):
    if event.fwd_from:
        return
    userinput_str = event.pattern_match.group(1)
    if not userinput_str:
        return await edit_delete(
            event,
            "Which category Chats should i list ?\nCheck .listall",
            parse_mode=parse_pre,
        )
    keyword = catinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    if no_of_chats == 0:
        return await edit_delete(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    userevent = await edit_or_reply(
        event, f"Fetching info of the category {keyword}", parse_mode=parse_pre
    )
    resultlist = f"**The category '{keyword}' have '{no_of_chats}' chats and these are listed below :**\n\n"
    errorlist = ""
    for chat in chats:
        try:
            chatinfo = await event.client.get_entity(int(chat))
            try:
                if chatinfo.broadcast:
                    resultlist += f" 👉 📢 **Channel** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{int(chat)}`\n\n"
                else:
                    resultlist += f" 👉 👥 **Group** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{int(chat)}`\n\n"
            except AttributeError:
                resultlist += f" 👉 👤 **User** \n  •  **Name : **{chatinfo.first_name} \n  •  **id : **`{int(chat)}`\n\n"
        except Exception:
            errorlist += f" 👉 __This id {int(chat)} in database probably you may left the chat/channel or may be invalid id.\
                            \nRemove this id from the database by using this command__ `.frmfrom {keyword} {int(chat)}` \n\n"
    finaloutput = resultlist + errorlist
    await edit_or_reply(catevent, finaloutput)


@borg.on(admin_cmd(pattern="listall$", command="listall"))
async def userbroadcast_list(event):
    if event.fwd_from:
        return
    if sql.num_broadcastlist_chats() == 0:
        return await edit_delete(
            event,
            "you haven't created at least one category  check info for more help",
            parse_mode=parse_pre,
        )
    chats = sql.get_broadcastlist_chats()
    resultext = "**Here are the list of your category's :**\n\n"
    for i in chats:
        resultext += f" 👉 `{i}` __contains {sql.num_broadcastlist_chat(i)} chats__\n"
    await edit_or_reply(event, resultext)


@borg.on(admin_cmd(pattern="frmfrom(?: |$)(.*)", command="frmfrom"))
async def userbroadcast_remove(event):
    if event.fwd_from:
        return
    userinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event, "From which category should i remove this chat", parse_mode=parse_pre
        )
    args = catinput_str.split(" ")
    if len(args) != 2:
        return await edit_delete(
            event,
            "Use proper syntax as shown .frmfrom category_name groupid",
            parse_mode=parse_pre,
        )
    try:
        groupid = int(args[0])
        keyword = args[1].lower()
    except ValueError:
        try:
            groupid = int(args[1])
            keyword = args[0].lower()
        except ValueError:
            return await edit_delete(
                event,
                "Use proper syntax as shown .frmfrom category_name groupid",
                parse_mode=parse_pre,
            )
    keyword = keyword.lower()
    check = sql.is_in_broadcastlist(keyword, int(groupid))
    if not check:
        return await edit_delete(
            event,
            f"This chat {groupid} is not in the category {keyword}",
            parse_mode=parse_pre,
        )
    sql.rm_from_broadcastlist(keyword, groupid)
    await edit_delete(
        event,
        f"This chat {groupid} is Now removed from the category {keyword}",
        parse_mode=parse_pre,
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is removed from category {keyword}",
                parse_mode=parse_pre,
            )
        except Exception:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is removed from category {keyword}",
                parse_mode=parse_pre,
            )


@borg.on(admin_cmd(pattern="delc(?: |$)(.*)", command="delc"))
async def userbroadcast_delete(event):
    if event.fwd_from:
        return
    userinput_str = event.pattern_match.group(1)
    check1 = sql.num_broadcastlist_chat(catinput_str)
    if check1 < 1:
        return await edit_delete(
            event,
            f"Are you sure that there is category {catinput_str}",
            parse_mode=parse_pre,
        )
    try:
        sql.del_keyword_broadcastlist(catinput_str)
        await edit_or_reply(
            event,
            f"Successfully deleted the category {catinput_str}",
            parse_mode=parse_pre,
        )
    except Exception as e:
        await edit_delete(
            event,
            str(e),
            parse_mode=parse_pre,
        )

CMD_HELP.update(
    {
        "broadcast":

        """╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.sendto category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __will send the replied message to all the chats in give category__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.fwdto category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __will forward the replied message to all the chats in give category__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.addto category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __It will add this chat/user/channel to the category of the given name__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.rmfrom category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __To remove the Chat/user/channel from the given category name__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.list category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Will show the list of all chats in the given category__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.listall`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Will show the list of all category names__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.frmfrom category_name chat_id`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __To force remove the given chat_id from the given category name usefull when you left that chat or banned you there__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `delc category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Deletes the category completely in database__
"""
    }
)

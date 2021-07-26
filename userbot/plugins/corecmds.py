import asyncio
import os
from datetime import datetime
from pathlib import Path

from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd, load_module, remove_plugin
from userbot.manager.utils import edit_or_reply

DELETE_TIMEOUT = 5
thumb_image_path = "./resources/Tamiluserbot.jpg"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "TamilBot"


@borg.on(admin_cmd(pattern="install$"))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await edit_or_reply(
                    event,
                    "Installed Plugin `{}`".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                await edit_or_reply(
                    event, "Errors! This plugin is already installed/pre-installed."
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await edit_or_reply(event, str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@borg.on(admin_cmd(pattern=r"send (?P<shortname>\w+)$", outgoing=True))
async def send(event):
    if event.fwd_from:
        return
    reply_to_id = None
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        caat = await event.client.send_file(  # pylint:disable=E0602
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
        )
        end = datetime.now()
        ms = (end - start).seconds
        await event.delete()
        await caat.edit(
            f"__**➥ Plugin Name:- {input_str} .**__\n__**➥ Uploaded in {ms} seconds.**__\n__**➥ Uploaded by :-**__ {DEFAULTUSER}"
        )
    else:
        await edit_or_reply(event, "404: File Not Found")


@borg.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$", outgoing=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await edit_or_reply(event, f"Unloaded {shortname} successfully")
    except Exception as e:
        await edit_or_reply(
            event, "Successfully unload {shortname}\n{}".format(shortname, str(e))
        )


@borg.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$", outgoing=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await edit_or_reply(event, f"Successfully loaded {shortname}")
    except Exception as e:
        await edit_or_reply(
            event,
            f"Could not load {shortname} because of the following error.\n{str(e)}",
        )

CMD_HELP.update(
    {
        "Corecmds":

        """╼•∘ 🅲🅼🅽🅳 ∘•╾ : `.install`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ : __Reply to any external plugin to install in bot__ 
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾ : `.load <plugin name>`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ : __To load that plugin again__
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾ : `.send <plugin name>`  
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ : __to send any plugin__
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾ : `.unload <plugin name>`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ : __To stop functioning of that plugin__ 
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾ : `.uninstall <plugin name>`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ : __To stop functioning of that plugin and remove that plugin from bot__ 
  
**Note : **__To unload a plugin permenantly from bot set __`NO_LOAD`__ var in heroku with that plugin name with space between plugin names__"""
    }
)

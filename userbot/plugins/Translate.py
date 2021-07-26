from asyncio import sleep

from googletrans import LANGUAGES, Translator
from userbot.utils import admin_cmd
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.plugins.sql_helper.globals import addgvar, gvarstatus
from userbot.manager.utils import edit_delete, edit_or_reply

@borg.on(admin_cmd(pattern="tl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif ";" in input_str:
        lan, text = input_str.split(";")
    else:
        await edit_delete(event, "`.tl LanguageCode` as reply to a message", time=5)
        return
    lan = lan.strip()
    Translator()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        output_str = f"**TRANSLATED from {LANGUAGES[translated.src].title()} to {LANGUAGES[lan].title()}**\
                \n`{after_tr_text}`"
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_delete(event, str(exc), time=5)


@bot.on(admin_cmd(outgoing=True, pattern=r"trt(?: |$)([\s\S]*)"))
async def translateme(trans):
    if trans.fwd_from:
        return
    textx = await trans.get_reply_message()
    message = trans.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(trans, "`Give a text or reply to a message to translate!`")
        return
    TRT_LANG = gvarstatus("TRT_LANG") or "en"
    try:
        reply_text = await getTranslate(deEmojify(message), dest=TRT_LANG)
    except ValueError:
        await edit_delete(trans, "`Invalid destination language.`", time=5)
        return
    source_lan = LANGUAGES[f"{reply_text.src.lower()}"]
    transl_lan = LANGUAGES[f"{reply_text.dest.lower()}"]
    reply_text = f"**From {source_lan.title()}({reply_text.src.lower()}) to {transl_lan.title()}({reply_text.dest.lower()}) :**\n`{reply_text.text}`"

    await edit_or_reply(trans, reply_text)
    if BOTLOG:
        await trans.client.send_message(
            BOTLOG_CHATID,
            f"`Translated some {source_lan.title()} stuff to {transl_lan.title()} just now.`",
        )


@borg.on(admin_cmd(pattern="lang trt (.*)", outgoing=True))
async def lang(value):
    if value.fwd_from:
        return
    arg = value.pattern_match.group(1).lower()
    if arg in LANGUAGES:
        addgvar("TRT_LANG", arg)
        LANG = LANGUAGES[arg]
    else:
        await edit_or_reply(
            value,
            f"`Invalid Language code !!`\n`Available language codes for TRT`:\n\n`{LANGUAGES}`",
        )
        return
    await edit_or_reply(value, f"`Language for Translator changed to {LANG.title()}.`")
    if BOTLOG:
        await value.client.send_message(
            BOTLOG_CHATID, f"`Language for Translator changed to {LANG.title()}.`"
        )


# https://github.com/ssut/py-googletrans/issues/234#issuecomment-722379788
async def getTranslate(text, **kwargs):
    translator = Translator()
    result = None
    for _ in range(10):
        try:
            result = translator.translate(text, **kwargs)
        except Exception:
            translator = Translator()
            await sleep(0.1)
    return result


CMD_HELP.update(
    {
        "translate": "**Plugin :** `translate`\
         \n\n╼•∘ 🅲🅼🅽🅳 ∘•╾ : `.tl LanguageCode <text/reply>`\
         \n ╼•∘ 🆄🆂🅰🅶🅴 ∘•╾ : __Translates given language to destination language. For <text> use .tl LanguageCode ; <text>__\
         \n\n╼•∘ 🅲🅼🅽🅳 ∘•╾ : `.trt <Reply/text>`\
         \n ╼•∘ 🆄🆂🅰🅶🅴 ∘•╾ : __It will translate your messege__\
         \n\n╼•∘ 🅲🅼🅽🅳 ∘•╾ : `.lang trt LanguageCode`\
         \n ╼•∘ 🆄🆂🅰🅶🅴 ∘•╾ : __It will set default langaugeCode for __**trt**__ command__\
         \n\n**•  Check here ** [Language codes](https://telegra.ph/Language-codes-05-19)\
        "
    }
)

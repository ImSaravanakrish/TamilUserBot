"""Fetch App Details from Playstore.
.app <app_name> to fetch app details.
.appr <app_name>  to fetch app details with Xpl0iter request link.
"""

# Ported by Poco Poco

import requests

import bs4

import re



from telethon import *

from userbot import CMD_HELP

from userbot.events import register
from userbot.utils import admin_cmd



#@register(pattern="^.app (.*)")
@borg.on(admin_cmd(pattern="app (.*)"))

async def apk(e):

    try:

        app_name = e.pattern_match.group(1)

        remove_space = app_name.split(' ')

        final_name = '+'.join(remove_space)

        page = requests.get("https://play.google.com/store/search?q="+final_name+"&c=apps")

        lnk = str(page.status_code)

        soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')

        results = soup.findAll("div","ZmHEEd")

        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text

        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text

        app_dev_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']

        app_rating = results[0].findNext('div', 'Vpfmgd').findNext('div', 'pf5lIe').find('div')['aria-label']

        app_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']

        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']

        app_details = "<a href='"+app_icon+"'>ð²&#8203;</a>"

        app_details += " <b>"+app_name+"</b>"

        app_details += "\n\n<code>Developer :</code> <a href='"+app_dev_link+"'>"+app_dev+"</a>"

        app_details += "\n<code>Rating :</code> "+app_rating.replace("Rated ", "â­ ").replace(" out of ", "/").replace(" stars", "", 1).replace(" stars", "â­ ").replace("five", "5")

        app_details += "\n<code>Features :</code> <a href='"+app_link+"'>View in Play Store</a>"

        app_details += "\n\n===> @TamilSupport <==="

        await e.edit(app_details, link_preview = True, parse_mode = 'HTML')

    except IndexError:

        await e.edit("தேடலில் எந்த முடிவும் கிடைக்கவில்லை. தயவுசெய்து உள்ளீடவும் **Valid app name**")

    except Exception as err:

        await e.edit("Exception Occured:- "+str(err))



#@register(pattern="^.appr (.*)")
@borg.on(admin_cmd(pattern="appr (.*)"))
async def apkr(e):

    try:

        app_name = e.pattern_match.group(1)

        remove_space = app_name.split(' ')

        final_name = '+'.join(remove_space)

        page = requests.get("https://play.google.com/store/search?q="+final_name+"&c=apps")

        lnk = str(page.status_code)

        soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')

        results = soup.findAll("div","ZmHEEd")

        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text

        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text

        app_dev_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']

        app_rating = results[0].findNext('div', 'Vpfmgd').findNext('div', 'pf5lIe').find('div')['aria-label']

        app_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']

        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']

        app_details = "<a href='"+app_icon+"'>ð²&#8203;</a>"

        app_details += " <b>"+app_name+"</b>"

        app_details += "\n\n<code>Developer :</code> <a href='"+app_dev_link+"'>"+app_dev+"</a>"

        app_details += "\n<code>Rating :</code> "+app_rating.replace("Rated ", "â­ ").replace(" out of ", "/").replace(" stars", "", 1).replace(" stars", "â­ ").replace("five", "5")

        app_details += "\n<code>Features :</code> <a href='"+app_link+"'>View in Play Store</a>"

        app_details += "\n\n<b>Download : </b> <a href='https://t.me/IndianBot_Official'>Request_Here by typing #request</a>"

        app_details += "\n\n⩴⩴⩥ @TamilSupport ⩤⩴⩴"

        await e.edit(app_details, link_preview = True, parse_mode = 'HTML')

    except IndexError:

        await e.edit("தேடலில் எந்த முடிவும் கிடைக்கவில்லை. தயவுசெய்து உள்ளீடவும் **Valid app name**")

    except Exception as err:

        await e.edit("Exception Occured:- "+str(err))
        
        
CMD_HELP.update(
    {
        "app": """**Plugin : ** `App`
        
  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.app <App Name>`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Get A Direct Download Link Of That App From Google Play Store__
    """
    }
)

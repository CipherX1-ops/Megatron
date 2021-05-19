# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from random import randrange
from re import compile as re_compile
from re import findall
from urllib.request import urlopen

import requests
import json
from bs4 import BeautifulSoup
from orangefoxapi import OrangeFoxAPI
from play_scraper import search
from search_engine_parser import GoogleSearch, YahooSearch
from telethon import Button
from telethon.tl.types import InputWebDocument as wb

from . import *
from . import humanbytes as hb

binpic = "https://telegra.ph/file/be4dd7375ef2313a43c41.jpg"
ippic = "https://telegra.ph/file/807e012dbe2789c0648ee.jpg"
ofox = "https://telegra.ph/file/231f0049fcd722824f13b.jpg"
gugirl = "https://telegra.ph/file/0df54ae4541abca96aa11.jpg"
yeah = "https://telegra.ph/file/e3c67885e16a194937516.jpg"
ps = "https://telegra.ph/file/de0b8d9c858c62fae3b6e.jpg"
ultpic = "https://telegra.ph/file/b2da137de76fc5cd85ffa.jpg"

ofox_api = OrangeFoxAPI()

@in_pattern("bin")
@in_owner
async def _(e):
    try:
        quer = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        kkkk = e.builder.article(
            title="Bin Checker",
            description="Give me your bin number",
            thumb=wb(binpic, 0, "image/jpeg", []),
            text="**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ Ⲃⲓⲛ Ⲥⲏⲉⲥⲕⲉʀ**\n\nYou didn't search any bin number",
            buttons=Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="bin ", same_peer=True),
        )
        await e.answer([kkkk])
    url = f"https://bins-su-api.vercel.app/api/{quer}"
    data = json.loads(requests.get(url).text) 
    search(quer)
    list = [] 
    results = data["result"]
    messages = data["message"]
    types = data["data"]["type"]
    bins = data["data"]["bin"]
    vendors = data["data"]["vendor"]
    levels = data["data"]["level"]
    banks = data["data"]["bank"]
    countrys = data["data"]["country"]
    text = """
**Ⳳⲁⳑⲓⲇⲓⲧⲩ**:- `{}`
**Ⲋⲧⲁⲧυⲋ**:- `{}`
**Ⲃⲓⲛ Ⲛυⲙⲃⲉʀ**:- `{}`
**Ⳳⲉⲛⲇⲟʀ**:- `{}`
**Ⳑⲉⳳⲉⳑ**:- `{}`
**Ⲧⲩⲣⲉ**:- `{}`
**Ⲃⲁⲛⲕ**:- `{}`
**Ⲥⲟυⲛⲧʀⲩ**:- `{}`
**✨ CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ Ⲃⲟⲧ ✨**
""".format(
            results,
            messages,
            bins,
            vendors,
            levels,
            types,
            banks,
            countrys,
        )
    but = [
        await e.builder.article(
            title=f"Bin Nuʍʙᴇr Sᴇᴀrᴄh Rᴇsulᴛ",
            description=f"{results}\n{messages}",
            text=text,
            thumb=wb(binpic, 0, "image/jpeg", []),
            link_preview=False,
            buttons=[
                [
                    Button.switch_inline(
                        "Sᴇᴀʀᴄʜ Aɢᴀɪɴ",
                        query="bin ",
                        same_peer=True,
                    ),
                    Button.switch_inline(
                        "Sʜᴀʀᴇ",
                        query=f"bin {quer}",
                        same_peer=False,
                    ),
                ],
            ],
        ),
    ] 
    await e.answer(but)
    
    

@in_pattern("ip")
@in_owner
async def _(e):
    try:
        quer = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        kkkk = e.builder.article(
            title="Ip Info",
            description="Give me an ip address",
            thumb=wb(ippic, 0, "image/jpeg", []),
            text="**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ ⲒⲢ Ⲓⲛϝⲟ**\n\nYou didn't search any ip address",
            buttons=Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="ip ", same_peer=True),
        )
        await e.answer([kkkk])
    url = f"http://ip-api.com/json/{quer}"
    data = json.loads(requests.get(url).text) 
    search(quer)
    list = [] 
    stat = data["status"]
    count = data["country"]
    countc = data["countryCode"]
    reg = data["region"]
    regn = data["regionName"]
    cit = data["city"]
    zp = data["zip"]
    lt = data["lat"]
    ln = data["lon"]
    tz = data["timezone"]
    or = data["org"]
    ass = data["as"]
    que = data["query"]
    linkk = "https://maps.google.com/?q={lt},{ln}"
    text = """
**IP Aɗɗrᥱss**:- `{}`
**𐍃ᴛᥲᴛᥙs**:- `{}`
**𑀝᧐ᥙᥒᴛry**:- `{}`
**𑀝᧐ᥙᥒᴛry 𑀝᧐ɗᥱ**:- `{}`
**Rᥱgi᧐ᥒ**:- `{}`
**Rᥱgi᧐ᥒ 𐌽ᥲⲙᥱ**:- `{}`
**𑀝iᴛy**:- `{}`
**Ziρ**:- `{}`
**𑀉ᥲᴛiᴛᥙɗᥱ**:- `{}`
**𑀉᧐ᥒgiᴛᥙɗᥱ**:- `{}`
**Tiⲙᥱ Z᧐ᥒᥱ**:- `{}`
**I𐍃P**:- `{}`
**𐌏RᏵ**:- `{}`
**A𐍃**:- `{}`
**𑀉᧐ᥴᥲᴛi᧐ᥒ 𑀉iᥒκ**:- [Link]({})

**✨ CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ Ⲃⲟⲧ ✨**
""".format(
            que,
            stat,
            count,
            countc,
            reg,
            regn,
            cit,
            zp,
            lt,
            ln,
            tz,
            or,
            ass,
            linkk,
        )
    but = [
        await e.builder.article(
            title=f"IP Iᥒf᧐rⲙᥲᴛi᧐ᥒ Rᥱsᥙᥣᴛ",
            description=f"{stat}\n{count}",
            text=text,
            thumb=wb(ippic, 0, "image/jpeg", []),
            link_preview=True,
            buttons=[
                [
                    Button.switch_inline(
                        "Sᴇᴀʀᴄʜ Aɢᴀɪɴ",
                        query="ip ",
                        same_peer=True,
                    ),
                    Button.switch_inline(
                        "Sʜᴀʀᴇ",
                        query=f"ip {quer}",
                        same_peer=False,
                    ),
                ],
            ],
        ),
    ] 
    await e.answer(but)


@in_pattern("ofox")
@in_owner
async def _(e):
    try:
        match = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        kkkk = e.builder.article(
            title="Enter Device Codename",
            thumb=wb(ofox, 0, "image/jpeg", []),
            text="**OFᴏx🦊Rᴇᴄᴏᴠᴇʀʏ**\n\nYou didn't search anything",
            buttons=Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="ofox ", same_peer=True),
        )
        await e.answer([kkkk])
    a = ofox_api.releases(codename=match)
    c = ofox_api.devices(codename=match)
    if len(a.data) > 0:
        fox = []
        for b in a.data:
            ver = b.version
            release = b.type
            size = hb(b.size)
            for z in c.data:
                fullname = z.full_name
                code = z.codename
                link = f"https://orangefox.download/device/{code}"
                text = f"**••OʀᴀɴɢᴇFᴏx Rᴇᴄᴏᴠᴇʀʏ Fᴏʀ•[•]({ofox})** {fullname}\n"
                text += f"**••Cᴏᴅᴇɴᴀᴍᴇ••** {code}\n"
                text += f"**••Bᴜɪʟᴅ Tʏᴘᴇ••** {release}\n"
                text += f"**••Vᴇʀsɪᴏɴ••** {ver}\n"
                text += f"**••Sɪᴢᴇ••** {size}\n"
                fox.append(
                    await e.builder.article(
                        title=f"{fullname}",
                        description=f"{ver}\n{release}",
                        text=text,
                        thumb=wb(ofox, 0, "image/jpeg", []),
                        link_preview=True,
                        buttons=[
                            Button.url("Dᴏᴡɴʟᴏᴀᴅ", url=f"{link}"),
                            Button.switch_inline(
                                "Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="ofox ", same_peer=True
                            ),
                        ],
                    )
                )
        await e.answer(fox)
    else:
        sed = e.builder.article(
            title="Not Found",
            description="Wrong Codename",
            text="OʀᴀɴɢFᴏx Rᴇᴄᴏᴠᴇʀʏ Fᴏʀ Yᴏᴜʀ Pʜᴏɴᴇ Is Eɪᴛʜᴇʀ Nᴏᴛ Oғғɪᴄɪᴀʟʟʏ Bᴜɪʟᴛ Oʀ Yᴏᴜ Hᴀᴠᴇ Eɴᴛᴇʀᴇᴅ Wʀᴏɴɢ Cᴏᴅᴇɴᴀᴍᴇ",
            buttons=Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="ofox ", same_peer=True),
        )
        await e.answer([sed])


@in_pattern("file ?(.*)")
@in_owner
async def _(e):
    file_path = e.pattern_match.group(1)
    file_name = file_path.split("/")[-1]
    bitton = [
        [
            Button.inline("anonfiles", data=f"flanonfiles//{file_path}"),
            Button.inline("transfer", data=f"fltransfer//{file_path}"),
        ],
        [
            Button.inline("bayfiles", data=f"flbayfiles//{file_path}"),
            Button.inline("x0", data=f"flx0//{file_path}"),
        ],
        [
            Button.inline("file.io", data=f"flfile.io//{file_path}"),
            Button.inline("siasky", data=f"flsiasky//{file_path}"),
        ],
    ]
    try:
        lnk = e.builder.article(
            title="file",
            text=f"**File:**\n{file_name}",
            buttons=bitton,
        )
    except BaseException:
        lnk = e.builder.article(
            title="file",
            text="File not found",
        )
    await e.answer([lnk])


@callback(
    re_compile(
        "fl(.*)",
    ),
)
@owner
async def _(e):
    t = (e.data).decode("UTF-8")
    data = t[2:]
    host = data.split("//")[0]
    file = data.split("//")[1]
    file_name = file.split("/")[-1]
    await e.edit(f"Uploading... `{file_name}` on {host}")
    await dloader(e, host, file)

@in_pattern("cipherx")
@in_owner
async def repo(e):
    res = [
        await e.builder.article(
            title="CɪᴘʜᴇʀX Bᴏᴛ",
            description="CɪᴘʜᴇʀX Bᴏᴛ | Telethon",
            thumb=wb(ultpic, 0, "image/jpeg", []),
            text="• **CɪᴘʜᴇʀX Suᴩᴇr Tᴇᴄhnᴏlᴏgy Bᴏᴛ** •",
            buttons=[
                [Button.url("•CɪᴘʜᴇʀX Bᴏᴛ•", url="t.me/CipherXBot")],
                [Button.url("•Sᴜᴘᴘᴏʀᴛ Chᴀnnᴇl•", url="t.me/FutureTechnologyOfficial")],
            ],
        ),
    ]
    await e.answer(res)
    
    
@in_pattern("go")
@in_owner
async def gsearch(q_event):
    try:
        match = q_event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        kkkk = q_event.builder.article(
            title="Search Something",
            thumb=wb(gugirl, 0, "image/jpeg", []),
            text="**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ Gᴏᴏɢʟᴇ Sᴇᴀʀᴄʜ**\n\nYou didn't search anything",
            buttons=Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="go ", same_peer=True),
        )
        await q_event.answer([kkkk])
    searcher = []
    page = findall(r"page=\d+", match)
    cache = False
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page), bool(cache))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"👉[{title}]({link})\n`{desc}`\n\n"
            searcher.append(
                await q_event.builder.article(
                    title=title,
                    description=desc,
                    thumb=wb(gugirl, 0, "image/jpeg", []),
                    text=f"**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ Gᴏᴏɢʟᴇ Sᴇᴀʀᴄʜ**\n\n**••Tɪᴛʟᴇ••**\n`{title}`\n\n**••Dᴇsᴄʀɪᴘᴛɪᴏɴ••**\n`{desc}`",
                    link_preview=False,
                    buttons=[
                        [Button.url("Lɪɴᴋ", url=f"{link}")],
                        [
                            Button.switch_inline(
                                "Sᴇᴀʀᴄʜ Aɢᴀɪɴ",
                                query="go ",
                                same_peer=True,
                            ),
                            Button.switch_inline(
                                "Sʜᴀʀᴇ",
                                query=f"go {match}",
                                same_peer=False,
                            ),
                        ],
                    ],
                ),
            )
        except IndexError:
            break
    await q_event.answer(searcher)

@in_pattern("yahoo")
@in_owner
async def gsearch(q_event):
    try:
        match = q_event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        kkkk = q_event.builder.article(
            title="Search Something",
            thumb=wb(yeah, 0, "image/jpeg", []),
            text="**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ Yᴀʜᴏᴏ Sᴇᴀʀᴄʜ**\n\nYou didn't search anything",
            buttons=Button.switch_inline(
                "Sᴇᴀʀᴄʜ Aɢᴀɪɴ",
                query="yahoo ",
                same_peer=True,
            ),
        )
        await q_event.answer([kkkk])
    searcher = []
    page = findall(r"page=\d+", match)
    cache = False
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page), bool(cache))
    gsearch = YahooSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"👉[{title}]({link})\n`{desc}`\n\n"
            searcher.append(
                await q_event.builder.article(
                    title=title,
                    description=desc,
                    thumb=wb(yeah, 0, "image/jpeg", []),
                    text=f"**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ Yᴀʜᴏᴏ Sᴇᴀʀᴄʜ**\n\n**••Tɪᴛʟᴇ••**\n`{title}`\n\n**••Dᴇsᴄʀɪᴘᴛɪᴏɴ••**\n`{desc}`",
                    link_preview=False,
                    buttons=[
                        [Button.url("Lɪɴᴋ", url=f"{link}")],
                        [
                            Button.switch_inline(
                                "Sᴇᴀʀᴄʜ Aɢᴀɪɴ",
                                query="yahoo ",
                                same_peer=True,
                            ),
                            Button.switch_inline(
                                "Sʜᴀʀᴇ",
                                query=f"yahoo {match}",
                                same_peer=False,
                            ),
                        ],
                    ],
                ),
            )
        except IndexError:
            break
    await q_event.answer(searcher)


@in_pattern("app")
@in_owner
async def _(e):
    try:
        f = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        kkkk = e.builder.article(
            title="Search Something",
            thumb=wb(ps, 0, "image/jpeg", []),
            text="**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ Pʟᴀʏ Sᴛᴏʀᴇ**\n\nYou didn't search anything",
            buttons=Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="app ", same_peer=True),
        )
        await e.answer([kkkk])
    foles = []
    aap = search(f)
    for z in aap:
        name = z["title"]
        desc = z["description"]
        price = z["price"]
        dev = z["developer"]
        icon = z["icon"]
        url = z["url"]
        ids = z["app_id"]
        text = f"**••Aᴘᴘ Nᴀᴍᴇ••** [{name}]({icon})\n"
        text += f"**••Dᴇᴠᴇʟᴏᴘᴇʀ••** `{dev}`\n"
        text += f"**••Pʀɪᴄᴇ••** `{price}`\n\n"
        text += f"**••Dᴇsᴄʀɪᴘᴛɪᴏɴ••**\n`{desc}`"
        foles.append(
            await e.builder.article(
                title=name,
                description=ids,
                thumb=wb(ps, 0, "image/jpeg", []),
                text=text,
                link_preview=True,
                buttons=[
                    [Button.url("Lɪɴᴋ", url=f"https://play.google.com{url}")],
                    [
                        Button.switch_inline(
                            "Mᴏʀᴇ Aᴘᴘs",
                            query="app ",
                            same_peer=True,
                        ),
                        Button.switch_inline(
                            "Sʜᴀʀᴇ",
                            query=f"app {f}",
                            same_peer=False,
                        ),
                    ],
                ],
            ),
        )
    await e.answer(foles)


@in_pattern("mods")
@in_owner
async def _(e):
    try:
        quer = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        kkkk = e.builder.article(
            title="Search Something",
            text="**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ Mᴏᴅᴅᴇᴅ Aᴘᴘs**\n\nYou didn't search anything",
            buttons=Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="mods ", same_peer=True),
        )
        await e.answer([kkkk])
    page = 1
    start = (page - 1) * 3 + 1
    urd = randrange(1, 3)
    if urd == 1:
        da = "AIzaSyAyDBsY3WRtB5YPC6aB_w8JAy6ZdXNc6FU"
    if urd == 2:
        da = "AIzaSyBF0zxLlYlPMp9xwMQqVKCQRq8DgdrLXsg"
    if urd == 3:
        da = "AIzaSyDdOKnwnPwVIQ_lbH5sYE4FoXjAKIQV0DQ"
    url = f"https://www.googleapis.com/customsearch/v1?key={da}&cx=25b3b50edb928435b&q={quer}&start={start}"
    data = requests.get(url).json()
    search_items = data.get("items")
    search(quer)
    modss = []
    for a in search_items:
        title = a.get("title")
        desc = a.get("snippet")
        link = a.get("link")
        text = f"**••Tɪᴛʟᴇ••** `{title}`\n\n"
        text += f"**Dᴇsᴄʀɪᴘᴛɪᴏɴ** `{desc}`"
        modss.append(
            await e.builder.article(
                title=title,
                description=desc,
                text=text,
                link_preview=True,
                buttons=[
                    [Button.url("Dᴏᴡɴʟᴏᴀᴅ", url=f"{link}")],
                    [
                        Button.switch_inline(
                            "Mᴏʀᴇ Mᴏᴅs",
                            query="mods ",
                            same_peer=True,
                        ),
                        Button.switch_inline(
                            "Sʜᴀʀᴇ",
                            query=f"mods {quer}",
                            same_peer=False,
                        ),
                    ],
                ],
            ),
        )
    await e.answer(modss)


@in_pattern("clipart")
@in_owner
async def clip(e):
    try:
        quer = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        kkkk = e.builder.article(
            title="Search Something",
            text="**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ Cʟɪᴘᴀʀᴛ Sᴇᴀʀᴄʜ**\n\nYou didn't search anything",
            buttons=Button.switch_inline(
                "Sᴇᴀʀᴄʜ Aɢᴀɪɴ",
                query="clipart ",
                same_peer=True,
            ),
        )
        await e.answer([kkkk])
    quer = quer.replace(" ", "+")
    sear = f"https://clipartix.com/search/{quer}"
    html = urlopen(sear)
    bs = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
    resul = bs.find_all("img", "attachment-full size-full")
    buil = e.builder
    hm = []
    for res in resul:
        hm += [buil.photo(include_media=True, file=res["src"])]
    await e.answer(hm, gallery=True)

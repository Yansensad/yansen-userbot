# Port By @VckyouuBitch From Geez-Projects
# # Copyright (C) 2021 Geez-Project
import asyncio

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import lepin_cmd


@lepin_cmd(pattern="ftyping(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Starting Fake Typing For {t} sec.`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@lepin_cmd(pattern="faudio(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Starting Fake audio recording For {t} sec.`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@lepin_cmd(pattern="fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Starting Fake video recording For {t} sec.`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@lepin_cmd(pattern="fgame(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Starting Fake Game Playing For {t} sec.`")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)


CMD_HELP.update(
    {
        "fakeaction": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ftyping` <jumlah teks>\
   \nUsage : Seakan akan sedang mengetik padahal tidak\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}faudio` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake audio\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}fgame` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake game\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}fvideo` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake video"
    }
)

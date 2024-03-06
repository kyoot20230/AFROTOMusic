import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["الزعيم","مطور السورس","مبرمج السورس"],"")
)
async def yas(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/59258f178623e4109f62a.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[سورس ميوزك الزعيم](https://t.me/EEEW2)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @T_5_G ❫
◉ 𝙸𝙳      : ❪ `7118337980` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@T_5_G)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "سورس ميوزك الزعيم", url=f"https://t.me/T_5_G"), 
                 ],[
                   InlineKeyboardButton(
                        "「سورس ميوزك الزعيم」", url=f"https://t.me/T_5_G"),
                ],

            ]

        ),

    )
@app.on_message(command(["تخ"]) & filters.group)
async def huhh(client, message):
    to_id = int(ahmed.split("to")[-1].split("in")[0])
    from_id = int(ahmed.split("ahmed")[-1].split("to")[0])
    in_id = int(caption.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    ahmed = message.text
    await message.reply_animation(
        animation=f"https://graph.org/file/0dcc6d8776f5486169077.mp4",
        caption=f"""↯︙قتل ↫ ⦗ {app.get_chat(to_id).first_name}]({to_url}) ⦘\nالضحيه دا 😢 ↫ ⦗ [{app.get_chat(from_id).first_name}]({from_url}) ⦘\nانا لله وانـا اليـه راجعـون 😢😢""",
    )
    reply_markup=InlineKeyboardMarkup(

       [
           [
               InlineKeyboardButton(
                   "‹ : 𝖬𝖺𝖳𝗋𝗂x 𝖳𝖾𝖠𝗆 : ›", url=f"https://t.me/EEEW2"),
           ],
       ]
    ),
  

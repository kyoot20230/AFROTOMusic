import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","الزعيم","السورس", "سورس الزعيم"])
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/aa04832e375d5e429e93b.mp4",
        caption=f"""
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " قناة السورس  ", url=f"https://t.me/EEEW2"),
                   InlineKeyboardButton(
                    
                    " جروب السورس ", url=f"https://t.me/EEEW2"), 
                ],[    
                    InlineKeyboardButton(
                        "مطور السورس ", url=f"https://t.me/T_5_G"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )


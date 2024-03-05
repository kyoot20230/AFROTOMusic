from pyrogram.types import InlineKeyboardButton

import config
from AFROTOMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="المطور", user_id=config.OWNER_ID),
          
        ],
         [InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text="CHANNEL", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="GROUP", url=f"https://t.me/EEEW2"),
        ],
        [
         
            InlineKeyboardButton(
                text="⭓الزعيم✘عبود ♪",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="المطور", user_id=config.OWNER_ID),
            
        ],
         [InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text="CHANNEL", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="GROUP", url=f"https://t.me/YR_HX"),
        ],
        [
         
            InlineKeyboardButton(
                text="⭓الزعيم✘عبود ♪",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons

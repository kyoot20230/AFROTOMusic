from pyrogram.types import InlineKeyboardButton

import config
from AFROTOMusic import app


def start_panel(_):
    buttons = [
        [InlineKeyboardButton(text="父 الأوامر 父", callback_data="zzzback")],
        [
            InlineKeyboardButton(text="GROUP", url=f"https://t.me/YR_HX),
            InlineKeyboardButton(text="CHANNEL", url=config.SUPPORT_CHANNEL),
        ],
        [
        InlineKeyboardButton(text="المطور", user_id=config.OWNER_ID),
        ],
        [
        InlineKeyboardButton(
                text="⭓ADD✘ME",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
         [
            InlineKeyboardButton(text="GROUP", url=f"https://t.me/YR_HX),
            InlineKeyboardButton(text="CHANNEL", url=config.SUPPORT_CHANNEL),
        ],
        [
        InlineKeyboardButton(text="المطور", user_id=config.OWNER_ID),
        ],
        [
        InlineKeyboardButton(
                text="⭓ADD✘ME",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        ],
    ]
    return buttons

from pyrogram.types import InlineKeyboardButton

import config
from AFROTOMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="⭓ADD✘ME",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
          InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback"),
        ],
        [
            InlineKeyboardButton(text="ᗪEᐯEᒪOᑭEᖇ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᑕᕼᗩᑎᑎEᒪ", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="⭓ADD✘ME",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="⭓ADD✘ME",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
          InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback"),
        ],
        [
            InlineKeyboardButton(text="ᗪEᐯEᒪOᑭEᖇ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᑕᕼᗩᑎᑎEᒪ", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="⭓ADD✘ME",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons

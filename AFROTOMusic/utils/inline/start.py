from pyrogram.types import InlineKeyboardButton

import config
from AFROTOMusic import app


def start_panel(_):
    buttons = [
    [
         [InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text="ᗪEᐯEᒪOᑭEᖇ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᑕᕼᗩᑎᑎEᒪ", url=config.SUPPORT_CHANNEL),
        ],
                [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=Commands&admin=ban_users+restrict_members+delete_messages+add_admins+change_info+invite_users+pin_messages+manage_call+manage_chat+manage_video_chats+promote_members",
            )
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
       
InlineKeyboardButton(
            [
           [InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text="ᗪEᐯEᒪOᑭEᖇ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᑕᕼᗩᑎᑎEᒪ", url=config.SUPPORT_CHANNEL),
        ],
                [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=Commands&admin=ban_users+restrict_members+delete_messages+add_admins+change_info+invite_users+pin_messages+manage_call+manage_chat+manage_video_chats+promote_members",
            )
        ],
    ]
    return buttons

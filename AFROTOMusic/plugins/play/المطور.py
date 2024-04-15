from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AFROTOMusic import app
import config

@app.on_message(
    command(["المطور", "السورس", "المصنع"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/4159620b551a2bb676482.jpg",
        caption="• Dev Bot ↦ ميوزك \n ━━━━━━━━━━━━ \n • Dev ↦  @PI_Pll . ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᯓ𓆩𖡡𓏺.ادمـ𝝞ـــ ـ𖤓๋ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧ͜͡ـِْ๋͜ان.𓏺𖡡𓆪", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "", url=config.SUPPORT_CHANNEL
                    ),
                ],
            ]
        ),
    )

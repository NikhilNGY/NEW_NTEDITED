from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>╭────[ ᴍʏ ᴅᴇᴛᴀɪʟs ]────⍟\n├⍟ Mʏ Nᴀᴍᴇ : Nᴏᴛʜɪɴɢ \n├⍟ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Nikhil5757h'>Oᴡɴᴇʀ</a>\n├⍟ Cʜᴀɴɴᴇʟ : <a href='https://t.me/KR_PICTURE'>Cʟɪᴄᴋ Hᴇʀᴇ</a>\n├⍟ ɢʀᴏᴜᴘ : <a href='https://t.me/Interworld_groups'>Cʟɪᴄᴋ Hᴇʀᴇ</a>\n├⍟ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ: <a href='https://t.me/Nikhil5757h'>Cᴏɴᴛᴀᴄᴛ Oᴡɴᴇʀ</a>\n├⍟ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : V1.0 [ ꜱᴛᴀʙʟᴇ ]\n╰───────────────⍟</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("●  🔒 Cʟᴏꜱᴇ  ● ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

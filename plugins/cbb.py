from pyrogram import Client 
from bot import Bot
from config import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import __version__ as pyrogram_version
from database.database import add_user, del_user, full_userbase, present_user

__version__ = "1.0.0" 

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        new_text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Support Group :  <a href='https://t.me/+5dYQcJbrLkRmODJl'>Click here</a>\n○ Channel : @Dramafilez </b>"
        if query.message.text != new_text:
            await query.message.edit_text(
                text=new_text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')]
            ])
        )
    
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

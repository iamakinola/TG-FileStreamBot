# This file is a part of TG-FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


class Language(object):
    def __new__ (self, message: Message):
        if getattr(message.from_user, 'language_code', 'Unknown') in self.available:
            return getattr(self, getattr(message.from_user, 'language_code', self.en), self.en)
        else:
            return self.en

    available=['en', 'Test']

    class en(object):
        START_TEXT = """
<i>👋 Hᴇʏ,</i>{}\n
<i>I'm Filestreambot As Well Direct Links Generator, here is what i can do for you.</i>\n
<i>I ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴇxᴛᴇʀɴᴀʟ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ FOR VIDEOS, PICTURES, MUSIC, DOCS, PDF, SRT, ETC</i>\n
<i>Tʜɪs IS Pᴇʀᴍᴇᴀɴᴛ Lɪɴᴋ Wɪᴛʜ Fᴀsᴛᴇsᴛ Sᴘᴇᴇᴅ</i>\n
<i>LINKS GENERATED DO NOT EXPIRE AND IT CAN BE EMBED TO WEBSITES</i>\n
<b>💰FOR SERVER DONATION OR SUPPORT💰</b>\n 
<i>🧑‍CONTACT DEVELOPER @iamakinola</i>\n
<i>Cʟɪᴄᴋ ᴏɴ Hᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</i>\n
<i><u>🚸𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>\n
<b>🔞 SENDING PRONOGRAPHIC ᴄᴏɴᴛᴇɴᴛꜱ TO BOT MAY ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ.🔞</b>\n\n"""

        HELP_TEXT = """
<i>- Sᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ (ᴏʀ) FORWARED ᴍᴇᴅɪᴀ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.</i>
<i>- I ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴇxᴛᴇʀɴᴀʟ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ !.</i>
<i>- LINKS GENERATED DO NOT EXPIRE AND IT CAN BE EMBED TO WEBSITES</i>
<i>- LINKS GENERATED CAN BE STREAM</i>
<i>- ᴅᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ Wɪᴛʜ FASTEST SPEED</i>
<i>- FILE RESOLUTIONS AND SIZE REMAIN THE SAME>
<i>MY LINKS DO NOT EXPIRE AND IT CAN BE EMBED TO WEBSITES</i>\n
<u>🚸𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u>\n
<b>🔞 SENDING PRONOGRAPHIC ᴄᴏɴᴛᴇɴᴛꜱ TO BOT MAY ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ.🔞</b>\n
<i>Cᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ (ᴏʀ) ʀᴇᴘᴏʀᴛ ʙᴜɢꜱ</i> <b>: <a href='https://t.me/iamakinola</a></b>"""

        ABOUT_TEXT = """
<b>⚜ Mʏ ɴᴀᴍᴇ : AUTO FILE STREAM</b>\n
<b>🔸Vᴇʀꜱɪᴏɴ : 3.0.3.1</b>\n
<b>🔹Lᴀꜱᴛ ᴜᴘᴅᴀᴛᴇᴅ : [ 18-Feb-22 ] 12:36 AM</b>\n
<b>🧑‍💻DEVELOPED BY : OLANIYI AKINOLA</b>\n

"""

        stream_msg_text ="""
<b>💰FOR DONATION CONTACT DEVELOPER @iamakinola💰</b>\n
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <i>{}</i>\n
<b>🖥WATCH :</b> <i>{}</i>"""

    class Test(object):
        START_TEXT = """
<i>👋 Hᴇʏ in Russian,</i>{}\n
<i>I'm Telegram Files Streaming Bot As Well Direct Links Generator</i>\n
<i>Cʟɪᴄᴋ ᴏɴ Hᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</i>\n
<i><u>🚸𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>\n
<b>🔞 Pʀᴏɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</b>\n\n"""

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
        ],
        [InlineKeyboardButton("📢 Bot Channel", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close'),
        ],
        [InlineKeyboardButton("📢 Bot Channel", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close'),
        ],
        [InlineKeyboardButton("📢 Bot Channel", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    
    

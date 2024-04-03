import os
import dictionary
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Dictionary Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

START_TEXT = """Hello {},

I am simple Telegram Words Dictionary Bot. \
I can provide you the meaning of any word."""

HELP_TEXT = """--**More Help**--

- Just send a word to get the meaning of it.
- I will provide you the meaning of the word.
"""

ABOUT_TEXT = """--**About Me**--

- **Bot :** `Dictionary Bot`
- **Developer :**
  • [GitHub](https://github.com/FayasNoushad)
  • [Telegram](https://telegram.me/FayasNoushad)
- **Source :** [Click here](https://github.com/FayasNoushad/Telegram-Dictionary-Bot)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Feedback', url='https://telegram.me/FayasNoushad')
        ],
        [
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)


@Bot.on_callback_query()
async def cb_data(bot, message):
    
    if message.data == "home":
        await message.message.edit_text(
            text=START_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    
    elif message.data == "help":
        await message.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    
    elif message.data == "about":
        await message.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    
    else:
        await message.message.delete()
    

@Bot.on_message(filters.private & filters.command(["start"]))
async def sed_start_message(bot, message):
    
    await message.reply_text(
        text=START_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=START_BUTTONS
    )


@Bot.on_message(filters.private & filters.command(["help"]))
async def send_help(bot, message):
    
    await message.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=HELP_BUTTONS
    )


@Bot.on_message(filters.private & filters.command(["about"]))
async def send_about(bot, message):
    
    await message.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=ABOUT_BUTTONS
    )


@Bot.on_message(filters.private & filters.text)
async def send_dictionary_details(_, message):
    m = await message.reply_text(
        text="Searching...",
        quote=True
    )
    word = message.text
    details = dictionary.dictionary(word)
    await m.edit_text(
        text=details,
        disable_web_page_preview=True
    )


Bot.run()

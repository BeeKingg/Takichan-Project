from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>ð **Hello {message.from_user.mention}** â \n
**[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Is a bot designed to play music in your voice chat groups!**
**To see some commands for using this bot, click Â» /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "â á´á´á´ á´á´ á´á´ Êá´á´Ê É¢Êá´á´á´â â", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "á´á´¡É´á´Ê", url="https://t.me/SiniAkuSepongin"
                    ),
                    InlineKeyboardButton(
                        "á´á´á´á´á´á´s", url=f"https://t.me/{GROUP_SUPPORT}")
                ],[
                    InlineKeyboardButton(
                        "Êá´á´¡ á´á´ á´sá´ á´á´â ââ", callback_data="cbcmds"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    start = time()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    delta_ping = time() - start
    await message.reply_text(
        f"""<b>ð **Hello {message.from_user.mention()}** â</b>

â **I'm active and ready to play music!
â¢ Start time: `{START_TIME_ISO}`

> Click on button Â» ð **Command** and see all bot commands!
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ Support", url=f"https://t.me/{GROUP_SUPPORT}")
                ],
                [
                    InlineKeyboardButton(
                        "ð Command", callback_data="cbcmds"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>ð **Hello** {message.from_user.mention()}</b>
**Please press the button below to read the explanation and see the list of available commands !**

ð¡ Bot by @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=" HOW TO USE ME", callback_data=f"cbguide"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>ð **Hello {message.from_user.mention} welcome to the help menu !**</b>

**__In this menu you can open several available command menus, in each command menu there is also a brief explanation of each command__**

ð¡ Bot by @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "HELP", callback_data="cbhowtouse"
                    )
                ]
            ]
        )
    )


@Client.on_message(filters.command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
@authorized_users_only
async def ping_pong(client: Client, message: Message):
    start = time()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    delta_ping = time() - start
    await message.reply_text(
        f"**Pong !!** {delta_ping * 1000:.3f} ms\n"
        f"â¢ **uptime:** `{uptime}`\n"
        f"â¢ **start time:** `{START_TIME_ISO}`"
    )

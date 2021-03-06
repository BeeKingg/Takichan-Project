# (C) KennedyProject github.com/KennedyProject

from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME as bn, BOT_IMG, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME
from handlers.play import cb_admin_check


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


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await query.edit_message_text(
        f"""<b>๐๐ป **Hi, I'm {query.message.from_user.mention}!**</b>

**I'm active and ready to play music!
โข Start time: `{START_TIME_ISO}`
โข Click on the button ยป ๐ Commands and see all the bot commands!

๐ก Bot By @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ Support", url=f"https://t.me/{GROUP_SUPPORT}")
                ],
                [
                    InlineKeyboardButton(
                        "๐ Command", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbabout"))
async def cbabout(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>โ **About  [{bn}](https://t.me/{BOT_USERNAME})**</b> 

โ? **A powerfull bot for playing music for groups!

โ? Working with pyrogram

โ? Using Python 3.9.7

โ? Can play and download music or videos from YouTube

โ? I can make you happy

โ? For more info click /help

__{bn} licensed under the GNU General Public License v.3.0__

โข Updates channel @{UPDATES_CHANNEL}
โข Group Support @{GROUP_SUPPORT}
โข Assistant @{ASSISTANT_NAME}
โข Here is my [Owner](https://t.me/{OWNER_NAME})**

โ Wanna make your own bot music? try click Source button!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ษขสแดแดแด", url="https://t.me/PussyGenk"
                    ),
                    InlineKeyboardButton(
                        "สแดแดแดโ", callback_data="cbadvanced"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ Here is the help menu !</b>

**In this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

๐ก Bot by @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Basic Cmd", callback_data="cbbasic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ basic commands for bots

[GROUP SETTINGS]
/play (title) - play music via youtube
/ytp (title) - play music live
/stream (reply to audio) - play music via reply to audio
/playlist - view queue list
/song (title) - download music from youtube
/search (title) - search for music from youtube in detail
/video (title) - download music from youtube in detail
/lyrics (title) - search for lyrics
/shazam (reply audio) - for identifying song name
/q (reply text) - to make a quotes sticker
/id - to show your id or chat id
[ MORE ]
/alive - check alive bot
/start - starting bot
/ping - show current ping

๐ก Bot by @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await query.edit_message_text(
        f"""**เผ Holla I'm [{bn}](https://t.me/{BOT_USERNAME})**

เผ **I'm Working Properly**

เผ **Bot : 6.0 LATEST**

เผ **My Master : [{OWNER_NAME}](https://t.me/{OWNER_NAME})**

เผ **Service Uptime : `{uptime}`**

**Thanks For Using Me โฅ๏ธ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "แดสแดแดแด", callback_data="cbabout"
                    ),
                    InlineKeyboardButton(
                        "แดสแดษดษดแดส", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ command for group admin

/player - view playback status
/pause - pauses playing music
/resume - resume paused music
/skip - skip to next song
/end - mute the music
/userbotjoin - invite assistant to join the group
/musicplayer (on / off) - turn on / off the music player in your group

๐ก Bot by @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ **command for sudo**

**/userbotleaveall - remove assistant from all groups
/gcast - send global messages via assistant
/rmd - delete downloaded files

๐ก Bot by @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ **Command fun**

**/chika - check it yourself
/wibu - check it yourself
/asupan - check yourself
/truth - check yourself
/dare - check it yourself
/q - to make quotes text

๐ก Bot by @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**HOW TO USE THIS BOTT :**

**1.) First, add to your group.
2.) Then make admin with all permissions except anonymous admin.
3.) Add @{ASSISTANT_NAME} to your group or type `/userbotjoin` to invite assistant.
4.) Turn on voice chat first before playing music.

๐ก Bot by @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Command List", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ **Here is the help menu !</b>

**In this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

๐ก Bot by @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Basic Cmd", callback_data="cbbasic"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "๐ Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐๏ธ** HOW TO USE THIS BOT :**

**1.) First, add to your group.
2.) Then make admin with all permissions except anonymous admin.
3.) Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite assistant.
4.) Turn on voice chat first before playing music.

๐ก Bot by @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbstart"
                    )
                ]
            ]
        )
    )

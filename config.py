import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

#--------------------------------
load_dotenv()

#--------------------------------
API_ID = 20948356
API_HASH = "6b202043d2b3c4db3f4ebefb06f2df12"
BOT_TOKEN = "7964387907:AAETpSvaX6nahZ-OJFuPVne8lv9lEIpKDm4"
MONGO_DB_URI = "mongodb+srv://Combobot:Combobot@combobot.4jbtg.mongodb.net/?retryWrites=true&w=majority&appName=Combobot"

#--------------------------------
SUPERBAN_CHAT_ID = -1002819331022
STORAGE_CHANNEL_ID = -1002846500795
AUTHORS = [7337748194, 7394132959]

#--------------------------------
String_client_1 = "BQGPvYcAhUkfHf38wIvJ_KxeXhQ7McM6oBCteXPzd5DsP3qKHq4gV7WKwg-5r7j1X1Kgtzr6kVKBLRO8JW4VLXIlnKM-31qCIuC05o-rNuDnz3rXWHwPMRGMMrUlEisOAhSg6kp5-9Qa9bcAoIE3OQj3WpOTTNR57diTMojazxUc7MN2zBs8MXrQ5os9FzvKfh9Sg6TvRvvHBjLLMQn6CR8dtXXPyJI3mrTMy7GOIlUKk1eYHep_U_2jnpHFLmNEWOSdbh7F33q4wcnVVbAbf4C859f_lLOF4RgYVHdQqYoglM2tBzJs8aArcHaw5KVRu_0BqwTOSJi-y2WzVCgcXSYVA36yMgAAAAHR1tKRAA"
String_client_2 = "BQAAC1MAA7e7ICp5bdyubr5EQAJRV7G2kOgTBH_Ko7kE146ngnhK_uiVoZ85wuSHU7EBJR5C_4nawxobjmcYkF8gd76DcNuftG5rHhvFQ2yvqiYdD2N6KVG1xywsqdDv-6Ob3huy_BCnyO0XUQZAHd3q1rc6DJFTz9vfdC4baWxxwNe2RuRFR7RKVs-Nk5Mqm9aMuJ8xNvoFqyJ59SShIDcOa35AzFk5_JI_M5vOktdESWkhdgZbpz2MQoMsZdHkImSEcwuOX410RXDyM60bJYVyk01mE1xI3Mi9cvZCVo8sbx5VmqTBzBT1FSKA4kBfnlSYdoo1qJoJq6-3bLenT4KAVvZMvgAAAABsFRQ_AA"
String_client_3 = ""
Mustjoin = "TeamScott"

#--------------------------------
SUPERBAN_REQUEST_TEMPLATE = """ᴀᴘᴘʀᴏᴠᴇ sᴜᴘᴇʀʙᴀɴ ꜰᴏʀ ᴜꜱᴇʀ :
{user_first}
ᴜꜱᴇʀ ɪᴅ : {user_id}

ʀᴇQᴜᴇꜱᴛ ꜰʀᴏᴍ ᴄʜᴀᴛ ɪᴅ : {chat_id}
ʀᴇQᴜᴇꜱᴛ ꜰʀᴏᴍ ᴄʜᴀᴛ ɴᴀᴍᴇ : {chat_name}

ʀᴇᴀꜱᴏɴ : {reason}
ʀᴇQᴜᴇꜱᴛ ʙʏ : {request_by}

ᴅᴀᴛᴇ & ᴛɪᴍᴇ : {ind_time}
ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}

ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rScottbot"""

SUPERBAN_REQUEST_RESPONSE = """ʏᴏᴜʀ sᴜᴘᴇʀʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ꜱᴇɴᴅᴇᴅ ᴛᴏ ᴛᴇᴀᴍ

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ʀᴇQᴜᴇꜱᴛ ʙʏ : {request_by}

ʏᴏᴜʀ ʀᴇQᴜᴇꜱᴛ ᴡɪʟʟ ʙᴇ ᴄʜᴇᴄᴋᴇᴅ ᴀɴᴅ ɪꜰ ɪᴛ'ꜱ ɢᴇɴᴜɪɴ ᴛʜᴇɴ ʙᴇ ꜱᴜʀᴇ ɪᴛ ᴡɪʟʟ ʙᴇ ᴀᴘᴘʀᴏᴠᴇᴅ.
ᴛʜᴀɴᴋꜜs ꜰᴏʀ ʏᴏᴜʀ sᴜᴘᴇʀʙᴀɴ ʀᴇQᴜᴇꜱᴛ

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : @TeamScott
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rScottbot"""

SUPERBAN_APPROVED_TEMPLATE = """ʏᴏᴜʀ sᴜᴘᴇʀʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ, ɴᴏᴡ ꜱᴛᴀʀᴛɪɴɢ sᴜᴘᴇʀʙᴀɴ.....

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ ᴀᴜᴛʜᴏʀ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rScottbot"""

SUPERBAN_DECLINED_TEMPLATE = """ʏᴏᴜʀ sᴜᴘᴇʀʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴅᴇᴄʟɪɴᴇᴅ

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ᴅᴇᴄʟɪɴᴇᴅ ʙʏ ᴀᴜᴛʜᴏʀ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rScottbot"""

SUPERBAN_COMPLETE_TEMPLATE = """sᴜᴘᴇʀʙᴀɴ ɪꜱ ᴄᴏᴍᴘʟᴇᴛᴇᴅ.

ᴜꜱᴇʀ : {user_first}
ᴜꜱᴇʀ ɪᴅ : {user_id}

ʀᴇᴀꜱᴏɴ : {reason}
ᴛᴏᴛᴀʟ ʙᴀɴ ɪɴ ꜰᴇᴅꜱ : {fed_count}
ɢʙᴀɴ ɪɴ : {extra_bans}

ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴛɪᴍᴇ ᴛᴀᴋᴇɴ : {time_taken}

ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : @TeamScott
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rScottbot"""

#--------------------------------
SUPERUNBAN_REQUEST_TEMPLATE = """ᴀᴘᴘʀᴏᴠᴇ sᴜᴘᴇʀᴜɴʙᴀɴ ꜰᴏʀ ᴜꜱᴇʀ :
{user_first}
ᴜꜱᴇʀ ɪᴅ : {user_id}

ʀᴇQᴜᴇꜱᴛ ꜰʀᴏᴍ ᴄʜᴀᴛ ɪᴅ : {chat_id}
ʀᴇQᴜᴇꜱᴛ ꜰʀᴏᴍ ᴄʜᴀᴛ ɴᴀᴍᴇ : {chat_name}

ʀᴇᴀꜱᴏɴ : {reason}
ʀᴇQᴜᴇꜱᴛ ʙʏ : {request_by}

ᴅᴀᴛᴇ & ᴛɪᴍᴇ : {ind_time}
ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}

ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rScottbot"""

SUPERUNBAN_REQUEST_RESPONSE = """ʏᴏᴜʀ sᴜᴘᴇʀᴜɴʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ꜱᴇɴᴅᴇᴅ ᴛᴏ ᴛᴇᴀᴍ

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀᴜɴʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ʀᴇQᴜᴇꜱᴛ ʙʏ : {request_by}

ʏᴏᴜʀ ʀᴇQᴜᴇꜱᴛ ᴡɪʟʟ ʙᴇ ᴄʜᴇᴄᴋᴇᴅ ᴀɴᴅ ɪꜰ ɪᴛ'ꜱ ɢᴇɴᴜɪɴ ᴛʜᴇɴ ʙᴇ ꜱᴜʀᴇ ɪᴛ ᴡɪʟʟ ʙᴇ ᴀᴘᴘʀᴏᴠᴇᴅ.
ᴛʜᴀɴᴋꜜs ꜰᴏʀ ʏᴏᴜʀ sᴜᴘᴇʀᴜɴʙᴀɴ ʀᴇQᴜᴇꜱᴛ

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : @TeamScott
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rScottbot"""

SUPERUNBAN_APPROVED_TEMPLATE = """ʏᴏᴜʀ sᴜᴘᴇʀᴜɴʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ, ɴᴏᴡ ꜱᴛᴀʀᴛɪɴɢ sᴜᴘᴇʀᴜɴʙᴀɴ.....

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀᴜɴʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ ᴀᴜᴛʜᴏʀ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rScottbot"""

SUPERUNBAN_DECLINED_TEMPLATE = """ʏᴏᴜʀ sᴜᴘᴇʀᴜɴʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴅᴇᴄʟɪɴᴇᴅ

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀᴜɴʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ᴅᴇᴄʟɪɴᴇᴅ ʙʏ ᴀᴜᴛʜᴏʀ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rScottbot"""

SUPERUNBAN_COMPLETE_TEMPLATE = """sᴜᴘᴇʀᴜɴʙᴀɴ ɪꜱ ᴄᴏᴍᴘʟᴇᴛᴇᴅ.

ᴜꜱᴇʀ : {user_first}
ᴜꜱᴇʀ ɪᴅ : {user_id}

ʀᴇᴀꜱᴏɴ : {reason}
ᴛᴏᴛᴀʟ ᴜɴʙᴀɴ ɪɴ ꜰᴇᴅꜱ : {fed_count}
ɢᴜɴʙᴀɴ ɪɴ : {extra_bans}

ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴛɪᴍᴇ ᴛᴀᴋᴇɴ : {time_taken}

ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : @TeamScott
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @rScottbot"""
#--------------------------------

START_VIDEO = "https://i.ibb.co/nsyp67FS/Img2url-bot.jpg"
HELP_MENU_VIDEO = "https://i.ibb.co/Z64Z3yCR/Img2url-bot.jpg"

#--------------------------------
LOGGER_ID = -1002059639505
STATS_VIDEO = "https://i.ibb.co/tMyDNvS2/Img2url-bot.jpg"
OWNER_ID = 7394132959

#--------------------------------
CLIENT_CHAT_DATA = [
    {
        "session": String_client_1,
        "chat_ids": [-1002746914942],
        "messages": [
            "/Joinfed 1111-aaaa",
            "/fban {user_id} {reason} \n\nApproved by {approver} \nTime: {utc_time}"
        ]
    },
    {
        "session": String_client_2,
        "chat_ids": [-1002871771020],
        "messages": [
            "/Joinfed 2222-bbbb",
            "/fban {user_id} Reason: {reason} \n\nDone by {approver}"
        ]
    },
    {
        "session": String_client_3,
        "chat_ids": [-1003333333333],
        "messages": [
            "/Joinfed 3333-cccc",
            "Ban user {user_id} - Reason: {reason} - By: {approver}"
        ]
    },
]

#--------------------------------
CLIENT_CHAT_DATA2 = [
    {
        "session": String_client_1,
        "chat_ids": [-1002746914942],
        "messages": [
            "/Joinfed 1111-aaaa",
            "/fban {user_id} {reason} \n\nApproved by {approver} \nTime: {utc_time}"
        ]
    },
    {
        "session": String_client_2,
        "chat_ids": [-1002222222222],
        "messages": [
            "/Joinfed 2222-bbbb",
            "/fban {user_id} Reason: {reason} \n\nDone by {approver}"
        ]
    },
    {
        "session": String_client_3,
        "chat_ids": [-1003333333333],
        "messages": [
            "/Joinfed 3333-cccc",
            "Ban user {user_id} - Reason: {reason} - By: {approver}"
        ]
    },
]

#--------------------------------

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

#--------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/rscottlogs")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TeamScott")

#--------------------------------
if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://")

if SUPPORT_CHAT:
    if not re.match(r"(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://")
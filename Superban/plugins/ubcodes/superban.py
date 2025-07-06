from pyrogram import Client, filters
from Superban import app
import asyncio
import logging
from config import (
    API_ID, API_HASH, BANNED_USERS,
    SUPERBAN_REQUEST_TEMPLATE,
    SUPERBAN_REQUEST_RESPONSE,
    SUPERBAN_APPROVED_TEMPLATE,
    SUPERBAN_DECLINED_TEMPLATE,
    SUPERBAN_COMPLETE_TEMPLATE,
    String_client_1, String_client_2, String_client_3
)
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from Superban.utils import get_readable_time
from pytz import timezone
from datetime import timedelta, datetime
import base64

reason_storage = {}
next_reason_id = 1

def store_reason(reason):
    global next_reason_id
    reason_id = next_reason_id
    reason_storage[reason_id] = reason
    next_reason_id += 1
    return reason_id

AUTHORS = [7337748194, 7202110938, 7512713188, 1813320767]
SUPPORT_CHAT_ID = -1002408883218
SUPPORT_CHANNEL_ID = -1002059806687

SPECIFIC_CHAT_IDS = [
    -1002390573482,
    -1002454747325,
    -1002165698624,
    -1002302258143,
    -1002320242726
]

STRING_SESSIONS = [String_client_1, String_client_2, String_client_3]

async def get_user_id(user_query):
    try:
        if user_query.isdigit():
            return int(user_query)
        user_query = user_query.lstrip('@')
        user = await app.get_users(user_query)
        return user.id
    except Exception as e:
        logging.error(f"Error fetching user ID for {user_query}: {e}")
        return None

async def retry_operation(func, *args, retries=1, delay=4):
    for attempt in range(retries):
        try:
            return await func(*args)
        except Exception as e:
            logging.error(f"Error on attempt {attempt + 1}: {e}")
            await asyncio.sleep(delay)
    return None

async def send_request_message(user, reason, action, message):
    reason_id = store_reason(reason) if reason else None
    chat_name = message.chat.title if message.chat.title else "Private Chat"
    chat_id = message.chat.id
    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
    utc_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    encoded_reason = base64.b64encode(str(reason_id).encode()).decode() if reason_id else ""

    request_message = await app.send_message(
        SUPPORT_CHAT_ID,
        SUPERBAN_REQUEST_TEMPLATE.format(
            user_first=user.first_name,
            user_id=user.id,
            chat_id=chat_id,
            chat_name=chat_name,
            reason=reason if reason else "No reason provided",
            request_by=message.from_user.first_name,
            ind_time=ind_time,
            utc_time=utc_time,
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✯ ᴀᴘᴘʀᴏᴠᴇ ✯", callback_data=f"{action}_approve_{user.id}_{encoded_reason}")],
            [InlineKeyboardButton("✯ ᴅᴇᴄʟɪɴᴇ ✯", callback_data=f"{action}_decline_{user.id}_{encoded_reason}")]
        ])
    )
    return request_message

@Client.on_message(filters.command(["superban"], prefixes=["."]) & (filters.group | filters.channel | filters.private) & filters.me)
async def super_ban(_, message):
    reason = None
    user_id = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        reason = message.reply_to_message.text
    else:
        msg_parts = message.text.split(None, 1)
        if len(msg_parts) > 1:
            user_query = msg_parts[1].split()[0]
            user_id = await get_user_id(user_query)
            reason = " ".join(msg_parts[1].split()[1:]) if len(msg_parts[1].split()) > 1 else None

    if user_id is None:
        await message.reply("Please specify a user ID, username, or reply to a message.")
        return

    try:
        user = await app.get_users(user_id)
    except Exception as e:
        logging.error(f"Error fetching user with ID {user_id}: {e}")
        await message.reply("User not found or inaccessible.")
        return

    await send_request_message(user, reason, "Super_Ban", message)
    utc_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    await message.reply(
        SUPERBAN_REQUEST_RESPONSE.format(
            user_first=user.first_name,
            reason=reason if reason else "No reason provided",
            request_by=message.from_user.first_name,
            utc_time=utc_time,
        )
    )
    await message.delete()

@app.on_callback_query(filters.regex(r'^Super_Ban_(approve|decline)(\d+)(.+)$'))
async def handle_super_ban_callback(client: Client, query: CallbackQuery):
    try:
        status, user_id_str, encoded_reason = query.data.split("_")[2:]
        user_id = int(user_id_str)
        reason_id = base64.b64decode(encoded_reason).decode()
        reason = reason_storage.get(int(reason_id), "No reason provided")
        user = await app.get_users(user_id)
    except Exception as e:
        logging.error(f"Callback data parsing error: {e}")
        await query.answer("Error occurred while processing.", show_alert=True)
        return

    if query.from_user.id not in AUTHORS:
        await query.answer("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀɴ ᴀᴜᴛʜᴏʀ", show_alert=True)
        return

    approval_author = query.from_user.first_name

    try:
        if status == "approve":
            await query.answer("ꜱᴜᴘᴇʀʙᴀɴ ᴀᴘᴘʀᴏᴠᴇᴅ.", show_alert=True)
            asyncio.create_task(super_ban_action(user_id, query.message, approval_author, reason))

            await query.message.edit(
                SUPERBAN_APPROVED_TEMPLATE.format(
                    user_first=user.first_name,
                    reason=reason,
                    approval_author=approval_author,
                    utc_time=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                )
            )
            notification_message = await app.send_message(SUPPORT_CHAT_ID, f"ꜱᴜᴘᴇʀʙᴀɴ ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ {approval_author}.")
            await asyncio.sleep(10)
            await query.message.delete()
            await notification_message.delete()

        elif status == "decline":
            await query.answer("ꜱᴜᴘᴇʀʙᴀɴ ᴅᴇᴄʟɪɴᴇᴅ.", show_alert=True)
            await query.message.edit(
                SUPERBAN_DECLINED_TEMPLATE.format(
                    user_first=user.first_name,
                    reason=reason,
                    approval_author=approval_author,
                    utc_time=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                )
            )
            notification_message = await app.send_message(SUPPORT_CHAT_ID, f"ꜱᴜᴘᴇʀʙᴀɴ ᴅᴇᴄʟɪɴᴇᴅ ʙʏ {approval_author}.")
            await asyncio.sleep(10)
            await query.message.delete()
            await notification_message.delete()

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        await query.answer("An unexpected error occurred. Please try again.", show_alert=True)

semaphore = asyncio.Semaphore(2)

async def send_message_with_semaphore(client, chat_id, msg):
    async with semaphore:
        result = await retry_operation(client.send_message, chat_id, msg)
        return result is not None

async def super_ban_action(user_id, message, approval_author, reason):
    try:
        user = await app.get_users(user_id)
        number_of_chats = 0
        start_time = datetime.utcnow()

        messages = [
            f"/Joinfed 5a94ee24-29bb-492e-b707-4d5ad2e65bec",
            f"/Joinfed d1e0c43c-21e8-4052-a7a6-5498e4cd63e5",
            f"/fban {user_id} {reason} \n\nᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ {approval_author} \n\nᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} \n\nʙᴀɴ ᴀᴘᴘᴇᴀʟ: @Emxes_Appeal \nᴘᴏᴡᴇʀᴇᴅ ʙʏ: @TeamArona"
        ]

        async def start_client(index, string_token):
            client = Client(
                name=f"userbot_{index}",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=string_token,
                plugins={"root": "Superban.plugins.userbot"},
            )
            await client.start()
            return client

        clients = await asyncio.gather(*(start_client(i + 1, s) for i, s in enumerate(STRING_SESSIONS) if s))

        async def send_messages(client):
            nonlocal number_of_chats
            for chat_id in SPECIFIC_CHAT_IDS:
                for msg in messages:
                    if await send_message_with_semaphore(client, chat_id, msg):
                        number_of_chats += 1
                    await asyncio.sleep(4)

        await asyncio.gather(*[send_messages(client) for client in clients])

        end_time = datetime.utcnow()
        time_taken = end_time - start_time
        readable_time = get_readable_time(time_taken)

        await app.send_message(SUPPORT_CHANNEL_ID,
            SUPERBAN_COMPLETE_TEMPLATE.format(
                user_first=user.first_name,
                user_id=user.id,
                reason=reason,
                fed_count=number_of_chats,
                approval_author=approval_author,
                utc_time=end_time.strftime('%Y-%m-%d %H:%M:%S'),
                time_taken=readable_time,
            )
        )
        await app.send_message(SUPPORT_CHAT_ID,
            SUPERBAN_COMPLETE_TEMPLATE.format(
                user_first=user.first_name,
                user_id=user.id,
                reason=reason,
                fed_count=number_of_chats,
                approval_author=approval_author,
                utc_time=end_time.strftime('%Y-%m-%d %H:%M:%S'),
                time_taken=readable_time,
            ),
            pin=True
        )
    except Exception as e:
        logging.error(f"Error during superban action: {e}")

if __name__ == "__main__":
    try:
        app.run()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        app.stop()
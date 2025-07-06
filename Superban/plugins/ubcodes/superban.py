from pyrogram import Client, filters
from Superban import app
import asyncio
import re
import logging
from config import (
    SUPERBAN_REQUEST_TEMPLATE,
    SUPERBAN_REQUEST_RESPONSE,
    SUPERBAN_APPROVED_TEMPLATE,
    SUPERBAN_DECLINED_TEMPLATE,
    SUPERBAN_COMPLETE_TEMPLATE,
    CLIENT_CHAT_DATA,
    SUPERBAN_CHAT_ID,
    STORAGE_CHANNEL_ID,
    AUTHORS
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pytz import timezone
from datetime import datetime
import base64
from Superban.core.mongo import group_log_db
from Superban.core.userbot import userbot_clients

def get_readable_time(duration):
    seconds = int(duration.total_seconds())
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    parts = []
    if days: parts.append(f"{days}d")
    if hours: parts.append(f"{hours}h")
    if minutes: parts.append(f"{minutes}m")
    if seconds: parts.append(f"{seconds}s")
    return ' '.join(parts) if parts else '0s'

reason_storage = {}
next_reason_id = 1

def store_reason(reason):
    global next_reason_id
    reason_id = next_reason_id
    reason_storage[reason_id] = reason
    next_reason_id += 1
    return reason_id

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
        SUPERBAN_CHAT_ID,
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

@app.on_callback_query(filters.regex(r'^Super_Ban_(approve|decline)_(\d+)_(.+)$'))
async def handle_super_ban_callback(client: Client, query: CallbackQuery):
    try:
        match = re.match(r'^Super_Ban_(approve|decline)_(\d+)_(.+)$', query.data)
        if not match:
            raise ValueError("Invalid callback data format")
        action, user_id_str, encoded_reason = match.groups()
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
        if action == "approve":
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
            try:
                await query.message.pin(disable_notification=True)
            except Exception as e:
                logging.warning(f"Could not pin approved message: {e}")
            notification_message = await app.send_message(SUPERBAN_CHAT_ID, f"ꜱᴜᴘᴇʀʙᴀɴ ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ {approval_author}.")
            await asyncio.sleep(10)
            await query.message.delete()
            await notification_message.delete()

        elif action == "decline":
            await query.answer("ꜱᴜᴘᴇʀʙᴀɴ ᴅᴇᴄʟɪɴᴇᴅ.", show_alert=True)
            await query.message.edit(
                SUPERBAN_DECLINED_TEMPLATE.format(
                    user_first=user.first_name,
                    reason=reason,
                    approval_author=approval_author,
                    utc_time=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                )
            )
            try:
                await query.message.pin(disable_notification=True)
            except Exception as e:
                logging.warning(f"Could not pin declined message: {e}")
            notification_message = await app.send_message(SUPERBAN_CHAT_ID, f"ꜱᴜᴘᴇʀʙᴀɴ ᴅᴇᴄʟɪɴᴇᴅ ʙʏ {approval_author}.")
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

        async def send_custom_messages(client, chat_ids, message_templates):
            nonlocal number_of_chats
            valid_chat_ids = []
            for chat_id in chat_ids:
                if await group_log_db.find_one({"chat_id": chat_id}):
                    valid_chat_ids.append(chat_id)
            for chat_id in valid_chat_ids:
                for template in message_templates:
                    msg = template.format(
                        user_id=user.id,
                        reason=reason,
                        approver=approval_author,
                        utc_time=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                    )
                    if await send_message_with_semaphore(client, chat_id, msg):
                        number_of_chats += 1
                    await asyncio.sleep(4)

        await asyncio.gather(*[
            send_custom_messages(userbot_clients[i], CLIENT_CHAT_DATA[i]["chat_ids"], CLIENT_CHAT_DATA[i]["messages"])
            for i in range(len(userbot_clients))
        ])

        end_time = datetime.utcnow()
        readable_time = get_readable_time(end_time - start_time)

        if await group_log_db.find_one({"chat_id": STORAGE_CHANNEL_ID}):
            await app.send_message(STORAGE_CHANNEL_ID,
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

        if await group_log_db.find_one({"chat_id": SUPERBAN_CHAT_ID}):
            final_msg = await app.send_message(SUPERBAN_CHAT_ID,
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
            try:
                await final_msg.pin(disable_notification=True)
            except Exception as e:
                logging.warning(f"Could not pin final completion message: {e}")
    except Exception as e:
        logging.error(f"Error during superban action: {e}")
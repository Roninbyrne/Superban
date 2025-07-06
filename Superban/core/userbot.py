from pyrogram import Client
from pyrogram.errors import SessionRevoked, AuthKeyInvalid
from Superban import LOGGER
from config import (
    API_ID,
    API_HASH,
    String_client_1,
    String_client_2,
    String_client_3,
    Mustjoin
)

string_sessions = [String_client_1, String_client_2, String_client_3]
userbot_clients = []

async def restart_bots():
    LOGGER("Userbot").info("🔄 Restarting all userbots...")
    for i, session in enumerate(string_sessions, start=1):
        if not session:
            LOGGER("Userbot").warning(f"⚠️ String_client_{i} is empty or not set, skipping...")
            continue

        try:
            client = Client(
                name=f"userbot_{i}",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=session,
                plugins={"root": "Superban.plugins.ubcodes"},
            )
            await client.start()
            me = await client.get_me()
            LOGGER("Userbot").info(f"🟢 String_client_{i} started as {me.first_name} (@{me.username})")

            try:
                await client.join_chat(Mustjoin)
                LOGGER("Userbot").info(f"📥 {me.first_name} joined {Mustjoin}")
            except Exception as join_err:
                LOGGER("Userbot").warning(f"⚠️ {me.first_name} failed to join {Mustjoin}: {join_err}")

            userbot_clients.append(client)

        except (SessionRevoked, AuthKeyInvalid):
            LOGGER("Userbot").error(f"🧟‍♂️ String_client_{i} is dead or revoked. Please generate a new one.")
        except Exception as e:
            LOGGER("Userbot").error(f"❌ Failed to start String_client_{i}: {e}")
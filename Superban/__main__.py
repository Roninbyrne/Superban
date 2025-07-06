import asyncio
import importlib
from pyrogram import idle
from Superban import LOGGER, app, start_bot
from Superban.plugins import ALL_MODULES
from Superban.core.chat_tracker import verify_groups_command
from Superban.core.userbot import restart_bots
from config import OWNER_ID

class DummyUser:
    id = OWNER_ID

class DummyMessage:
    from_user = DummyUser()

    async def reply_text(self, *args, **kwargs):
        pass

async def init():
    await restart_bots()

    await start_bot()

    for all_module in ALL_MODULES:
        importlib.import_module("Superban.plugins" + all_module)
    LOGGER("Superban.plugins").info("✅ Successfully imported all modules.")

    try:
        dummy_message = DummyMessage()
        await verify_groups_command(app, dummy_message)
        LOGGER("Superban").info("🔁 Automatically verified groups on startup.")
    except Exception as e:
        LOGGER("Superban").warning(f"⚠️ Failed to verify groups on startup: {e}")

    LOGGER("Superban").info("🚀 Superban Bot and Userbots Started Successfully.")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
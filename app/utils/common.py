from aiogram import Bot
from app.utils.logging_config import logging_topics
from app.core.config import config

bot = Bot(token=config.TELEGRAM_BOT_TOKEN)

async def log_to_telegram(module_name: str, message: str):
    chat_configs = logging_topics.get(module_name, None)
    if not chat_configs:
        raise ValueError(f"No logging configuration found for module: {module_name}")

    chat_id = chat_configs["chat_id"]
    topic_id = chat_configs["topic_id"]

    try:
        await bot.send_message(
            chat_id=chat_id,
            message_thread_id=topic_id,
            text=message,
            parse_mode="HTML",
            disable_web_page_preview=True,
            disable_notification=True
        )
    except:
        pass
import asyncio
import logging

from aiogram import Dispatcher
from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage

from core.settings import bot_settings


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s'
    )

    dispatcher = Dispatcher(storage=MemoryStorage())
    bot = Bot(token=bot_settings.bot_token.get_secret_value())

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(
        bot,
        allowed_updates=dispatcher.resolve_used_update_types()
    )


if __name__ == '__main__':
    asyncio.run(main())

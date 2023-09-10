import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from middleware.db_session import DBSessionMiddleware
from data.sql import SQLManager
from data import Base
from utils.logging import get_logger


async def main():
    from utils.logging import log

    bot = Bot(os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    log.debug("Bot created")

    from router import router

    dp.include_router(router.router)

    db = SQLManager(get_logger("db"))

    dp.update.middleware(DBSessionMiddleware(db.session))
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    Base.metadata.create_all(bind=db.engine)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
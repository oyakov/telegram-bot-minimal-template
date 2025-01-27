from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from oam import log_config
from service.telegram_service import TelegramService

logger = log_config.get_logger(__name__)

telegram_service = TelegramService()


async def initialize_advertiser(bot: Bot, interval_minutes: int = 1):
    """
    Initialize the periodic job for sending messages
    Job will run approximately every interval_minutes and will check if this time there are messages
    which schedule has arrived and send those messages to the configured list of chats
    """
    # logger.info("Initialize the advertiser job")
    # scheduler = AsyncIOScheduler()
    # scheduler.add_job(check_calendar, 'interval', args=[bot], minutes=interval_minutes)
    # scheduler.start()
    # logger.info("Advertiser is initialized")

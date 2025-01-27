from oam import log_config
from schedule.periodic_message_scheduler import initialize_advertiser
from subsystem.subsystem import Subsystem, InitPriority

logger = log_config.get_logger(__name__)


class SchedulerSubsystem(Subsystem):
    def __init__(self, bot, interval_minutes):
        self.bot = bot
        self.interval_minutes = interval_minutes

    async def initialize(self, subsystem_manager):
        logger.info(f"Initializing Scheduler subsystem {self.bot}, {self.interval_minutes}")
        await initialize_advertiser(bot=self.bot, interval_minutes=self.interval_minutes)
        self.is_initialized = True

    async def shutdown(self):
        pass

    # def get_router(self):
    #     return self.new_message_router

    def get_priority(self):
        return InitPriority.DATA_CONSUMPTION

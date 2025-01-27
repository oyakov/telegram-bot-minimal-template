from aiogram import Bot
from injector import Module, provider, singleton, multiprovider


from routers.base_router import BaseRouter

from subsystem.database_subsystem import DatabaseSubsystem
from subsystem.logger_subsystem import LoggerSubsystem
from subsystem.scheduler_subsystem import SchedulerSubsystem
from subsystem.slave_bot_subsystem import SlaveBotSubsystem
from subsystem.subsystem import Subsystem
from subsystem.subsystem_manager import SubsystemManager


class SubsystemManagerModule(Module):

    # Database client
    @singleton
    @provider
    def provide_database_subsystem(self) -> DatabaseSubsystem:
        return DatabaseSubsystem()

    # Logger configuration and provider - WARN! this is essential subsystem, do not remove it from the list
    @singleton
    @provider
    def provide_logger_subsystem(self) -> LoggerSubsystem:
        return LoggerSubsystem()

    # Use this do define and run scheduled jobs
    @singleton
    @provider
    def provide_scheduler_subsystem(self, bot: Bot) -> SchedulerSubsystem:
        return SchedulerSubsystem(bot, 1)


    # This subsystem will start a bot, TODO: need to be able to run multiple bots at once
    @singleton
    @provider
    def provide_slave_bot_subsystem(self, bot: Bot, routers: list[BaseRouter]) -> SlaveBotSubsystem:
        return SlaveBotSubsystem(bot, routers=routers)

    # Adjust this list by adding, commenting out or removing subsystems
    # This is the list of subsystems that is going to be started by Subsystem Manager
    @singleton
    @multiprovider
    def provide_subsystem_list(self,
                               database_subsystem: DatabaseSubsystem,
                               logger_subsystem: LoggerSubsystem,
                               scheduler_subsystem: SchedulerSubsystem,
                               ) -> list[Subsystem]:
        return [
            database_subsystem,
            logger_subsystem,
            scheduler_subsystem,
        ]

    # Subsystem manager starts and maintains all the variety of subsystems and inits them according to their priorities
    @singleton
    @provider
    def provide_subsystem_manager(
            self
    ) -> SubsystemManager:
        return SubsystemManager()

from injector import Module, singleton, provider, multiprovider

from routers.base_router import BaseRouter
from routers.gateway_router import GatewayRouter
from service.openai.openai_api_service import OpenAIAPIService

# This module specifies Routers which are the objects for Telegram dialogs tailored for various purpose
class RouterModule(Module):


    # this router list is going to be injected into the Bot
    @singleton
    @multiprovider
    def provide_router_list(self,
                            # This example how routers can be passed
                            # actuator_router: ActuatorRouter,
                            # binance_router: BinanceRouter,
                            # configuration_router: ConfigurationRouter,
                            # new_message_router: NewMessageRouter,
                            # openai_router: OpenAIRouter
                            ) -> list[BaseRouter]:
        return [
            # This example how routers can be passed
            # actuator_router,
            # binance_router,
            # configuration_router,
            # new_message_router,
            # openai_router
        ]

    # Gateway router is like API gateway for routers that can intercept message before getting to router
    # and filter it or apply some preprocessing
    @singleton
    @provider
    def provide_gateway_router(self, routers: list[BaseRouter]) -> GatewayRouter:
        return GatewayRouter(routers)

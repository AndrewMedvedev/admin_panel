import logging

from litestar import Litestar

from src.classes import config_logging
from src.errors import SendError, send_error

from .routers import (ChatsHistoryController, EventsController,
                      NotificationsController, SetCookieAndLogoutController,
                      UsersController, UsersWhoSharedContactsController)

config_logging(level=logging.INFO)

app = Litestar(
    route_handlers=[
        EventsController,
        UsersController,
        UsersWhoSharedContactsController,
        ChatsHistoryController,
        NotificationsController,
        SetCookieAndLogoutController,
    ],
    exception_handlers={SendError: send_error},
    debug=True,
)

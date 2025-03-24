import logging
from litestar import Litestar

from .routers import EventsController
from src.classes import config_logging

config_logging(level=logging.INFO)

app = Litestar(route_handlers=[EventsController], debug=True)

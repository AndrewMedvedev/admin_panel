from litestar import Controller, post

from src.classes import Notifications
from src.schemas import (CustomResponse, NotificationAllSchema,
                         NotificationPhoneNumberSchema)


class NotificationsController(Controller):
    path = "/api/v1/notifications"
    tags = ["Notifications"]

    def __init__(self, owner):
        super().__init__(owner)
        self.notifications = Notifications()

    @post(path="/notify-all")
    async def notify_all_post(
        self,
        data: NotificationAllSchema,
    ) -> CustomResponse:
        return await self.notifications.notify_all(schema=data)

    @post(path="/notify-by-phone-number")
    async def notify_by_phone_number_post(
        self,
        data: NotificationPhoneNumberSchema,
    ) -> CustomResponse:
        return await self.notifications.notify_by_phone_number(
            schema=data,
        )

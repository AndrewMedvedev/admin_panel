from litestar.status_codes import HTTP_200_OK

from src.config import Settings
from src.interfaces import NotificationsBase
from src.schemas import (CustomResponse, NotificationAllSchema,
                         NotificationPhoneNumberSchema)

from .get_data import GetData


class Notifications(NotificationsBase):
    def __init__(self) -> None:
        self.get_data = GetData()
        self.settings = Settings
        self.response = CustomResponse

    async def notify_all(
        self,
        schema: NotificationAllSchema,
    ) -> CustomResponse:
        result = await self.get_data.data_post(
            setting=self.settings.NOTIFICATIONS_ALL,
            params=schema.model_dump(),
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="contacts",
        )

    async def notify_by_phone_number(
        self,
        schema: NotificationPhoneNumberSchema,
    ) -> CustomResponse:
        result = await self.get_data.data_post(
            setting=self.settings.NOTIFICATIONS_BY_PHONE_NUMBER,
            params=schema.model_dump(),
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="contacts_count",
        )

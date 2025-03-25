from litestar.status_codes import HTTP_200_OK

from src.config import Settings
from src.interfaces import ChatsHistoryBase
from src.schemas import CustomResponse

from .get_data import GetData


class ChatsHistory(ChatsHistoryBase):
    def __init__(self) -> None:
        self.get_data = GetData()
        self.settings = Settings
        self.response = CustomResponse

    async def chats(self) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=self.settings.CHATS_HISTORY,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="contacts",
        )

    async def chats_count(self) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=self.settings.CHATS_HISTORY_COUNT,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="chats_count",
        )

    async def chats_per_day_count(self) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=self.settings.CHATS_HISTORY_PER_DAY_COUNT,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="chats_per_day_count",
        )

    async def chats_user_id(
        self,
        user_id: int,
        is_paginated: bool,
        page: int,
        limit: int,
    ) -> CustomResponse:
        data = {
            "is_paginated": str(is_paginated).lower(),
            "page": page,
            "limit": limit,
        }
        result = await self.get_data.data_get(
            setting=f"{self.settings.CHATS_HISTORY_USER_ID}{user_id}",
            params=data,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="chats_user_id",
        )

    async def chats_user_id_count(self, user_id: int) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=f"{self.settings.CHATS_HISTORY_USER_ID_COUNT}{user_id}/count/",
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="chats_user_id_count",
        )

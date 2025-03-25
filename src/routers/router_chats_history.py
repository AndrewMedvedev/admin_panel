from litestar import Controller, get
from litestar.params import Parameter

from src.classes import ChatsHistory
from src.schemas import CustomResponse


class ChatsHistoryController(Controller):
    path = "/api/v1/chats"
    tags = ["ChatsHistory"]

    def __init__(self, owner):
        super().__init__(owner)
        self.chats = ChatsHistory()

    @get(path="/")
    async def chats_get(self) -> CustomResponse:
        return await self.chats.chats()

    @get(path="/count")
    async def chats_count_get(self) -> CustomResponse:
        return await self.chats.chats_count()

    @get(path="/per-day-count")
    async def chats_per_day_count_get(self) -> CustomResponse:
        return await self.chats.chats_per_day_count()

    @get(path="/{user_id: int}")
    async def chats_user_id_get(
        self,
        user_id: int,
        is_paginated: bool = Parameter(
            query="is_paginated",
            required=False,
            default=False,
        ),
        page: int = Parameter(
            query="page",
            required=False,
            default=1,
        ),
        limit: int = Parameter(
            query="limit",
            required=False,
            default=10,
        ),
    ) -> CustomResponse:
        return await self.chats.chats_user_id(
            user_id=user_id,
            is_paginated=is_paginated,
            page=page,
            limit=limit,
        )

    @get(path="/{user_id: int}/count")
    async def chats_user_id_count_get(
        self,
        user_id: int,
    ) -> CustomResponse:
        return await self.chats.chats_user_id_count(user_id=user_id)

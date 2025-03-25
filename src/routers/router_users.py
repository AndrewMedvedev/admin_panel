from litestar import Controller, get

from src.classes import Users
from src.schemas import CustomResponse


class UsersController(Controller):
    path = "/api/v1/users"
    tags = ["Users"]

    def __init__(self, owner):
        super().__init__(owner)
        self.users = Users()

    @get(path="/")
    async def users_get(self) -> CustomResponse:
        return await self.users.users()

    @get(path="/count")
    async def users_count_get(self) -> CustomResponse:
        return await self.users.users_count()

    @get(path="/per-day-count")
    async def users_per_day_count_get(self) -> CustomResponse:
        return await self.users.users_per_day_count()

    @get(path="/{user_id: int}")
    async def users_user_id_get(
        self,
        user_id: int,
    ) -> CustomResponse:
        return await self.users.users_user_id(user_id=user_id)

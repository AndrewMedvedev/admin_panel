from litestar.status_codes import HTTP_200_OK

from src.config import Settings
from src.interfaces import UsersBase
from src.schemas import CustomResponse

from .get_data import GetData


class Users(UsersBase):
    def __init__(self) -> None:
        self.get_data = GetData()
        self.settings = Settings
        self.response = CustomResponse

    async def users(self) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=self.settings.USERS,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="users",
        )

    async def users_count(self) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=self.settings.USERS_COUNT,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="users_count",
        )

    async def users_per_day_count(self) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=self.settings.USERS_PER_DAY_COUNT,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="users_per_day_count",
        )

    async def users_user_id(self, user_id: int) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=f"{self.settings.USERS_USER_ID}{user_id}",
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="users_user_id",
        )

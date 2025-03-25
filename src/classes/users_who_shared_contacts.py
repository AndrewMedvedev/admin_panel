from litestar.status_codes import HTTP_200_OK

from src.config import Settings
from src.interfaces import UsersWhoSharedContactsBase
from src.schemas import CustomResponse

from .get_data import GetData


class UsersWhoSharedContacts(UsersWhoSharedContactsBase):
    def __init__(self) -> None:
        self.get_data = GetData()
        self.settings = Settings
        self.response = CustomResponse

    async def contacts(self) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=self.settings.USERS_W_S_C_CONTACTS,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="contacts",
        )

    async def contacts_count(self) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=self.settings.USERS_W_S_C_COUNT,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="contacts_count",
        )

    async def contacts_per_day_count(self) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=self.settings.USERS_W_S_C_PER_DAY_COUNT,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="contacts_per_day_count",
        )

    async def contacts_user_id(self, user_id: int) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=f"{self.settings.USERS_W_S_C_USER_ID}{user_id}",
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="contacts_user_id",
        )

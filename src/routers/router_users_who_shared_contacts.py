from litestar import Controller, get

from src.classes import UsersWhoSharedContacts
from src.schemas import CustomResponse


class UsersWhoSharedContactsController(Controller):
    path = "/api/v1/contacts"
    tags = ["UsersWhoSharedContacts"]

    def __init__(self, owner):
        super().__init__(owner)
        self.users = UsersWhoSharedContacts()

    @get(path="/")
    async def contacts_get(self) -> CustomResponse:
        return await self.users.contacts()

    @get(path="/count")
    async def contacts_count_get(self) -> CustomResponse:
        return await self.users.contacts_count()

    @get(path="/per-day-count")
    async def contacts_per_day_count_get(self) -> CustomResponse:
        return await self.users.contacts_per_day_count()

    @get(path="/{user_id: int}")
    async def contacts_user_id_get(
        self,
        user_id: int,
    ) -> CustomResponse:
        return await self.users.contacts_user_id(user_id=user_id)

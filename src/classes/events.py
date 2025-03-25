from litestar.status_codes import HTTP_200_OK

from src.config import Settings
from src.interfaces import EventsBase
from src.schemas import AddEventSchema, CustomResponse

from .get_data import GetData


class Events(EventsBase):

    def __init__(self) -> None:
        self.get_data = GetData()
        self.settings = Settings
        self.response = CustomResponse

    async def add_events(
        self,
        schema: AddEventSchema,
    ) -> CustomResponse:
        result = await self.get_data.data_post(
            params=schema.model_dump(),
            setting=self.settings.EVENTS_ADD,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="add_events",
        )

    async def get_events(self) -> CustomResponse:
        result = await self.get_data.data_get(
            setting=self.settings.EVENTS_GET,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="get_events",
        )

    async def delete_events(
        self,
        event_id: int,
    ) -> CustomResponse:
        result = await self.get_data.data_delete(
            setting=f"{self.settings.EVENTS_DELETE}{event_id}"
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_func="delete_events",
        )

from .get_data_class import GetData
from src.interfaces import EventsBase
from src.schemas import AddEventSchema
from src.config import Settings
from src.schemas import CustomResponse
from litestar.status_codes import HTTP_200_OK


class Events(EventsBase):

    def __init__(self) -> None:
        self.get_data = GetData()
        self.settings = Settings
        self.response = CustomResponse

    async def add_events(self, schema: AddEventSchema) -> CustomResponse:
        answer = await self.get_data.data_post(
            params=schema.model_dump(),
            setting=self.settings.EVENTS_ADD,
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=answer,
            message="Выполненно",
            name_endpoint="/api/v1/events/add",
        )

    async def get_events(self) -> CustomResponse:
        answer = await self.get_data.data_get_no_params(setting=self.settings.EVENTS_GET)
        return self.response(
            status_code=HTTP_200_OK,
            body=answer,
            message="Выполненно",
            name_endpoint="/api/v1/events/add",
        )

    async def delete_events(
        self,
        event_id: int,
    ) -> CustomResponse:
        answer = await self.get_data.data_delete(
            setting=f"{self.settings.EVENTS_DELETE}{event_id}"
        )
        return self.response(
            status_code=HTTP_200_OK,
            body=answer,
            message="Выполненно",
            name_endpoint="/api/v1/events/add",
        )


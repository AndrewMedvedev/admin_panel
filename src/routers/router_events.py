from litestar import Controller, get, post, delete
from src.schemas import AddEventSchema
from src.classes import Events
from litestar.status_codes import HTTP_200_OK
from src.schemas import CustomResponse



class EventsController(Controller):
    path = "/api/v1/events"

    def __init__(self, owner):
        super().__init__(owner)
        self.events = Events()

    @post(path="/add")
    async def add(self, data: AddEventSchema) -> CustomResponse:
        return await self.events.add_events(schema=data)

    @get(path="/get", status_code=HTTP_200_OK)
    async def get(self) -> CustomResponse:
        return await self.events.get_events()

    @delete(path="/delete/{event_id: int}", status_code=HTTP_200_OK)
    async def delete(self, event_id: int) -> CustomResponse:
        return await self.events.delete_events(event_id=event_id)

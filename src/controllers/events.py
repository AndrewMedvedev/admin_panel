from ..rest import EventsApi
from ..schemas import EventSchema


class EventControl:
    def __init__(self):
        self.api = EventsApi()

    async def create_event(self, schema: EventSchema) -> None:
        return await self.api.events_add(params=schema.to_dict())

    async def get_event(self, page: int, limit: int) -> dict:
        return await self.api.events_get(page=page, limit=limit)

    async def delete_event(self, event_id: int) -> None:
        return await self.api.events_delete(event_id=event_id)

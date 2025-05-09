from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse

from ..constants import PATH_ENDPOINT
from ..controllers import EventControl
from ..schemas import EventSchema

events_router = APIRouter(prefix=f"{PATH_ENDPOINT}events", tags=["events"])


@events_router.post("/add/")
async def add(schema: EventSchema) -> Response:
    await EventControl().create_event(schema)
    return Response(status_code=status.HTTP_201_CREATED)


@events_router.get("/get/")
async def get(page: int = 1, limit: int = 10) -> Response:
    result = await EventControl().get_event(page, limit)
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)


@events_router.delete("/delete/{event_id}")
async def delete(event_id: int) -> Response:
    await EventControl().delete_event(event_id=event_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

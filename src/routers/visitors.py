from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse

from ..constants import PATH_ENDPOINT
from ..controllers import VisitorControl

visitor_router = APIRouter(prefix=f"{PATH_ENDPOINT}visitors", tags=["visitors"])


@visitor_router.get("/verify/")
async def verify(unique_string: str) -> HTMLResponse:
    result = await VisitorControl().verify_visitor(unique_string=unique_string)
    return HTMLResponse(content=result, status_code=status.HTTP_200_OK)

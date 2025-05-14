from fastapi import APIRouter

from ..constants import PATH_ENDPOINT

test_router = APIRouter(prefix=f"{PATH_ENDPOINT}test", tags=["test"])


@test_router.get("/")
async def test_watchtower() -> str:
    return "hello nigga"

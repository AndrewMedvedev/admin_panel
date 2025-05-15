from fastapi import APIRouter

from ..constants import PATH_ENDPOINT

test_router = APIRouter(prefix=f"{PATH_ENDPOINT}test", tags=["test"])


@test_router.get("/")
async def test_watchtower() -> str:
    return "hello niggas"


@test_router.get("/fuck")
async def fuck() -> str:
    return "niggas i fuck everyone"


@test_router.get("/balerinacapuchina")
async def balerinacapuchina() -> str:
    return "balerinacapuchina"

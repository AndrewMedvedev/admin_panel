from fastapi import APIRouter, status
from fastapi.datastructures import UploadFile
from fastapi.param_functions import File, Form
from fastapi.responses import JSONResponse, Response

from ..constants import PATH_ENDPOINT
from ..controllers import NewsControl

news = APIRouter(prefix=f"{PATH_ENDPOINT}news", tags=["news"])


@news.post("/add/")
async def add(
    title: str = Form(),
    body: str = Form(),
    image: UploadFile | None = File(default=None),
) -> Response:
    await NewsControl().create_news(title=title, body=body, image=image)
    return Response(status_code=status.HTTP_201_CREATED)


@news.get("/get/")
async def get(page: int = 1, limit: int = 10) -> Response:
    result = await NewsControl().get_news(page=page, limit=limit)
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)


@news.delete("/delete/{news_id}")
async def delete(news_id: int) -> Response:
    await NewsControl().delete_news(news_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

from fastapi import UploadFile

from ..rest import NewsApi


class NewsControl:
    def __init__(self):
        self.api = NewsApi()

    async def create_news(self, title: str, body: str, image: UploadFile | None) -> None:
        return await self.api.news_add(title=title, body=body, image=image)

    async def get_news(self, page: int, limit: int) -> dict:
        return await self.api.news_get(page=page, limit=limit)

    async def delete_news(self, news_id: int) -> None:
        return await self.api.news_delete(news_id=news_id)

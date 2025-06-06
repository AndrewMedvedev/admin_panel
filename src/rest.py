from aiohttp import ClientSession, FormData
from fastapi import UploadFile

from config import settings

from .utils import valid_answer, valid_answer_html


class BaseApi:
    def __init__(self):
        self.settings = settings
        self.clientsession = ClientSession


class VisitorsApi(BaseApi):
    async def verify(self, unique_string: str) -> str:
        async with (
            self.clientsession() as session,
            session.get(url=f"{self.settings.VERIFY_VISITOR}{unique_string}") as data,
        ):
            return await valid_answer_html(response=data)


class EventsApi(BaseApi):
    async def events_add(self, params: dict) -> None:
        async with (
            self.clientsession() as session,
            session.post(url=self.settings.EVENTS_ADD, json=params, ssl=False) as data,
        ):
            return await valid_answer(response=data)

    async def events_get(self, page: int, limit: int) -> dict:
        async with (
            self.clientsession() as session,
            session.get(
                url=self.settings.EVENTS_GET,
                params={
                    "is_paginated": "true",
                    "page": page,
                    "limit": limit,
                },
                ssl=False,
            ) as data,
        ):
            return await valid_answer(data)

    async def events_delete(self, event_id: int) -> None:
        async with (
            self.clientsession() as session,
            session.delete(
                url=f"{self.settings.EVENTS_DELETE}{event_id}",
                ssl=False,
            ) as data,
        ):
            return await valid_answer(data)


class NewsApi(BaseApi):
    async def news_add(self, title: str, body: str, image: UploadFile | None) -> None:
        read_img = await image.read() if image is not None else None
        form_data = FormData()
        form_data.add_field(name="image", value=read_img, content_type="image/jpeg")
        form_data.add_field("title", title)
        form_data.add_field("body", body)
        async with (
            self.clientsession() as session,
            session.post(
                url=self.settings.NEWS_ADD,
                data=form_data,
                ssl=False,
            ) as data,
        ):
            return await valid_answer(data)

    async def news_get(self, page: int, limit: int) -> dict:
        async with (
            self.clientsession() as session,
            session.get(
                url=self.settings.NEWS_GET,
                params={
                    "is_paginated": "true",
                    "page": page,
                    "limit": limit,
                },
                ssl=False,
            ) as data,
        ):
            return await valid_answer(data)

    async def news_delete(self, news_id: int) -> None:
        async with (
            self.clientsession() as session,
            session.delete(
                url=f"{self.settings.NEWS_DELETE}{news_id}",
                ssl=False,
            ) as data,
        ):
            return await valid_answer(data)

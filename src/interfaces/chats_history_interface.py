from abc import ABC, abstractmethod

from src.schemas import CustomResponse


class ChatsHistoryBase(ABC):

    @abstractmethod
    async def chats() -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def chats_count() -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def chats_per_day_count() -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def chats_user_id() -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def chats_user_id_count() -> CustomResponse:
        raise NotImplementedError

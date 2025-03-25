from abc import ABC, abstractmethod

from src.schemas import CustomResponse


class NotificationsBase(ABC):

    @abstractmethod
    async def notify_all() -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def notify_by_phone_number() -> CustomResponse:
        raise NotImplementedError

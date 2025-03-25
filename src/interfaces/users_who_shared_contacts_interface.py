from abc import ABC, abstractmethod

from src.schemas import CustomResponse


class UsersWhoSharedContactsBase(ABC):

    @abstractmethod
    async def contacts() -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def contacts_count() -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def contacts_per_day_count() -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def contacts_user_id() -> CustomResponse:
        raise NotImplementedError

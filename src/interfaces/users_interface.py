from abc import ABC, abstractmethod

from src.schemas import CustomResponse


class UsersBase(ABC):

    @abstractmethod
    async def users() -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def users_count() -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def users_per_day_count() -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def users_user_id() -> CustomResponse:
        raise NotImplementedError

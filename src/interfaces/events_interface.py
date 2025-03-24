from abc import ABC, abstractmethod

from src.schemas import CustomResponse


class EventsBase(ABC):

    @abstractmethod
    async def add_events(self) -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def get_events(self) -> CustomResponse:
        raise NotImplementedError

    @abstractmethod
    async def delete_events(self) -> CustomResponse:
        raise NotImplementedError

from abc import ABC, abstractmethod


class EventsBase(ABC):

    @abstractmethod
    async def add_events(self):
        raise NotImplementedError

    @abstractmethod
    async def get_events(self):
        raise NotImplementedError

    @abstractmethod
    async def delete_events(self):
        raise NotImplementedError

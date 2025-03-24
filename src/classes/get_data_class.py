import logging
from aiohttp import ClientSession
from .controls import valid_answer

log = logging.getLogger(__name__)

class GetData:

    def __init__(self):
        self.session = ClientSession

    async def data_post(
        self,
        params: dict,
        setting: str,
    ):
        log.warning(params)
        async with self.session() as session:
            async with session.post(
                url=setting,
                json=params,
                ssl=False,
            ) as response:
                return await valid_answer(response=response)
            

    async def data_get(
        self,
        setting: str,
        params: dict = None,
    ):
        async with self.session() as session:
            async with session.get(
                url=setting,
                params=params,
                ssl=False,
            ) as response:
                return await valid_answer(response=response)
            

    async def data_get_no_params(
        self,
        setting: str,
    ):
        async with self.session() as session:
            async with session.get(
                url=setting,
                ssl=False,
            ) as response:
                return await valid_answer(response=response)
            

    async def data_delete(
        self,
        setting: str,
        params: dict = None,
    ):
        async with self.session() as session:
            async with session.delete(
                url=setting,
                params=params,
                ssl=False,
            ) as response:
                return await valid_answer(response=response)
            
    
            
    

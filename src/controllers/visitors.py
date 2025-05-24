from ..rest import VisitorsApi


class VisitorControl:
    def __init__(self):
        self.api = VisitorsApi()

    async def verify_visitor(self, unique_string: str) -> str:
        return await self.api.verify(unique_string=unique_string)

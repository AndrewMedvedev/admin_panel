from typing import Any

from pydantic import BaseModel


class CustomResponse(BaseModel):
    status_code: int
    body: Any
    message: str
    name_func: str

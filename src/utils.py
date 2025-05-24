from typing import Any

from .exeptions import BadRequestHTTPError, ExistsHTTPError, NoPlacesHTTPError, NotFoundHTTPError


async def valid_answer(response: Any) -> None:
    status = response.status
    match status:
        case 200:
            return await response.json()
        case 201:
            return None
        case 204:
            return None
        case 400:
            raise BadRequestHTTPError
        case 403:
            raise NoPlacesHTTPError
        case 404:
            raise NotFoundHTTPError
        case 409:
            raise ExistsHTTPError


async def valid_answer_html(response: Any) -> None:
    status = response.status
    match status:
        case 200:
            return await response.text()
        case 201:
            return None
        case 204:
            return None
        case 400:
            raise BadRequestHTTPError
        case 403:
            raise NoPlacesHTTPError
        case 404:
            raise NotFoundHTTPError
        case 409:
            raise ExistsHTTPError

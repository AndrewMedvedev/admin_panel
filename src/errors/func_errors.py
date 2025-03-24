from litestar import Request, Response
from litestar.status_codes import HTTP_401_UNAUTHORIZED

from src.schemas import CustomResponse

from .errors import SendError


def send_error(
    _: Request,
    exc: SendError,
) -> Response:
    return Response(
        content=CustomResponse(
            status_code=HTTP_401_UNAUTHORIZED,
            body=str(exc),
            message="Ошибка в выполнении",
            name_endpoint="_",
        ),
        status_code=HTTP_401_UNAUTHORIZED,
    )

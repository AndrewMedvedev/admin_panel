from litestar import Controller, Response, get
from litestar.status_codes import HTTP_200_OK


class SetCookieAndLogoutController(Controller):
    tags = ["SetCookie and Logout"]

    @get(path="/set/cookie/{access: str}/{refresh: str}")
    async def set_cookie(
        self,
        access: str,
        refresh: str,
    ) -> Response:
        response = Response(
            status_code=HTTP_200_OK,
            content={"message": "Cookie установлен"},
            media_type="application/json",
        )
        response.set_cookie(
            key="access",
            value=access,
            samesite="none",
            httponly=True,
            secure=True,
        )

        response.set_cookie(
            key="refresh",
            value=refresh,
            samesite="none",
            httponly=True,
            secure=True,
        )
        return response

    @get(path="/logout")
    async def logout(self) -> Response:
        response = Response(
            status_code=HTTP_200_OK,
            content={"message": "Вы успешно вышли из системы"},
            media_type="application/json",
        )
        response.delete_cookie(
            key="access",
            path="/",
        )
        response.delete_cookie(
            key="refresh",
            path="/",
        )
        return response

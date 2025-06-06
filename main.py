from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.exeptions import (
    BadRequestHTTPError,
    BaseHTTPError,
    HTTPException,
    InternalHTTPError,
    JSONError,
)
from src.middleware import MiddlewareValidTokens
from src.routers import events_router, news_router, visitor_router

app = FastAPI(title="Admin panel")


@app.exception_handler(Exception)
def handler(
    _request: Request,
    exception: Exception | BaseException,
    description: str | None = None,
) -> JSONResponse:
    if isinstance(exception, HTTPException):
        exception = BaseHTTPError(str(exception), exception.status_code)
    if isinstance(exception, BaseHTTPError):
        pass
    elif isinstance(exception, (AttributeError, ValueError, KeyError, TypeError)):
        description = description if description is not None else str(exception)
        exception = BadRequestHTTPError()

    else:
        exception = InternalHTTPError()

    return JSONResponse(
        content=JSONError.create(exception, description).to_dict(),
        status_code=exception.code,
    )


origins: list[str] = [
    "http://localhost:3000",
    "https://register-666-ramzer.onrender.com",
    "https://admin-panel-production-19ca.up.railway.app",
    "https://frontend-project-production-6352.up.railway.app",
    "https://admin-panel11.onrender.com",
    "https://online-service-for-applicants.onrender.com",
    "https://admin-panel2222.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.add_middleware(MiddlewareValidTokens)


def include_routers(app: FastAPI):
    app.include_router(visitor_router)
    app.include_router(events_router)
    app.include_router(news_router)


include_routers(app)

# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.fastapi_helper.exceptions import DefaultHTTPException

app = FastAPI()


class AuthException(DefaultHTTPException):
    code = "auth_error"
    type = "AuthError"
    message = "Auth error"
    status_code = status.HTTP_401_UNAUTHORIZED


@app.exception_handler(DefaultHTTPException)
async def http_exception_accept_handler(request: Request, exc: DefaultHTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=[{"code": exc.code, "type": exc.type, "message": exc.message}],
    )


@app.get("/")
async def root():
    raise AuthException()


uvicorn.run(app, host="localhost", port=8001)

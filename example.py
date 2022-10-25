# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from fastapi_helper.exceptions.validation_exceptions import init_validation_handler
from fastapi_helper.schemas.examples_generate import examples_generate
from src.fastapi_helper.exceptions import DefaultHTTPException


# create and initiates the necessary functions for the app
def create_app() -> FastAPI:
    app_ = FastAPI()
    init_validation_handler(app=app_)
    return app_


app = create_app()


# example auth exceptions and a handler that will intercept it
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


# some example model for post endpoint
class User(BaseModel):
    name: str
    surname: str
    password: str


@app.post(
    "/",
    responses=examples_generate.get_error_responses(
       AuthException,
       auth=True
    )
)
async def root(user: User):
    return user


uvicorn.run(app, host="localhost", port=8001)

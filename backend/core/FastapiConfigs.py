from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)

from core.database import engine
from sqlalchemy.ext.asyncio import create_async_engine
import config


class FastAPIConfigs:
    def __new__(cls, app: FastAPI):
        ExceptionHandlers(app)

    @classmethod
    @asynccontextmanager
    async def lifespan(cls, app: FastAPI):
        engine.async_engine = create_async_engine(config.DB_URL, echo=True)
        await engine.create_tables(engine.async_engine)
        yield
        await engine.async_engine.dispose()


class ExceptionHandlers:
    def __new__(cls, app: FastAPI):
        @app.exception_handler(HTTPException)
        async def fastapi_http_exception_handler(request, exc):
            return await http_exception_handler(request, exc)

        @app.exception_handler(StarletteHTTPException)
        async def custom_http_exception_handler(request, exc):
            return await http_exception_handler(request, exc)

        @app.exception_handler(RequestValidationError)
        async def validation_exception_handler(request, exc):
            return await request_validation_exception_handler(request, exc)

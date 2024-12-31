import logging

from aiohttp.abc import HTTPException
from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from starlette.responses import JSONResponse
from app.core.config import config

if config.DEBUG == 0:
    storage_uri = "redis://localhost:6379/0"
else:
    storage_uri = None


limiter = Limiter(
    key_func=lambda request: request.client.host if request.client else "unknown",
    storage_uri=storage_uri
)

def add_rate_limit_middleware(app: FastAPI):

    app.state.limiter = limiter
    app.add_middleware(SlowAPIMiddleware)
    app.add_exception_handler(RateLimitExceeded, rate_limit_handler)

async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=400,
        content={
            "ok": False,
            "error_code": 400,
            "description": "Too many requests! Please try again later",
        },
    )
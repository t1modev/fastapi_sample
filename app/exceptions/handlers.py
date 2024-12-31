from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = [
        {
            "field": error["loc"][-1],
            "message": error["msg"],
            "type": error["type"],
        }
        for error in exc.errors()
    ]
    description = f"Validation error: {details[0]['field']} {details[0]['type']}" if details else "Validation error"

    return JSONResponse(
        status_code=400,
        content={
            "ok": False,
            "error_code": 400,
            "description": description,
            "details": details,
        },
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=400,
        content={
            "ok": False,
            "error_code": exc.status_code,
            "description": exc.detail,
        },
    )

async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={
            "ok": False,
            "error_code": 500,
            "description": "Internal server error",
            "details": str(exc),
        },
    )
from fastapi import FastAPI
from app.api.routes import users
from app.docs.swagger import setup_swagger
from app.db.session import init_db
from fastapi.exceptions import RequestValidationError, HTTPException
from app.exceptions.handlers import (
    validation_exception_handler,
    http_exception_handler,
    global_exception_handler,
)
from app.middlewares.rate_limit import add_rate_limit_middleware


app = FastAPI()

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)


add_rate_limit_middleware(app)


app.include_router(users, prefix="/u", tags=["Users"])


setup_swagger(app)


@app.on_event("startup")
async def startup_event():
    await init_db()

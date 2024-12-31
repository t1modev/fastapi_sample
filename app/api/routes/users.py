from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from app.db.session import get_db
from app.db.models import User
from app.middlewares.rate_limit import limiter
from app.utils import log_to_telegram
router = APIRouter()

@router.get("/")
@limiter.limit("1/second")
async def get_users(request: Request,db: AsyncSession = Depends(get_db)):
    return {"1": 1}


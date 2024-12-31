from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, func, DECIMAL, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, unique=True, index=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=True)
    username = Column(String(255), unique=False, nullable=True, index=True)
    photo_url = Column(String(255), nullable=True)
    lang_code = Column(String(2), nullable=True, index=True)
    last_active = Column(DateTime, default=datetime.utcnow)

    is_banned = Column(Boolean, default=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=False, default=func.now())
    created_at = Column(DateTime, default=datetime.utcnow)




class Plans(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(33), nullable=False, default="default")  # default/custom
    conversion_rate = Column(DECIMAL(precision=10, scale=6), nullable=False)
    min_amount = Column(Integer, nullable=False)
    max_amount = Column(Integer, nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=False, default=func.now())
    created_at = Column(DateTime, default=datetime.utcnow)





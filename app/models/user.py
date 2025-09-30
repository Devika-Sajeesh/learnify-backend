from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    gpa = Column(Float)
    branch = Column(String)
    sem = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    subin = Column(String)   # subjects you're good at
    subnin = Column(String)  # subjects you struggle with


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db.base import Base
from datetime import datetime

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_text = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

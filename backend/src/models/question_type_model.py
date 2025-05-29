# sparkcard/backend/src/models/question_type_model.py
from sqlalchemy import Column, Integer, Text
from src.db.base import Base

class QuestionType(Base):
    __tablename__ = 'question_type'
    question_type_id = Column(Integer, primary_key=True)
    question_type_name = Column(Text, nullable=False, unique=True)
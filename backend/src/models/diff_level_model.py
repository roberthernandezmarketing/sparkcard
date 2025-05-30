# sparkcard/backend/src/models/diff_level_model.py
from sqlalchemy import Column, Integer, Text
from backend.src.db.base import Base

class DifficultyLevel(Base):
    __tablename__ = 'diff_level'
    diff_level_id = Column(Integer, primary_key=True)
    diff_level_name = Column(Text, nullable=False, unique=True)
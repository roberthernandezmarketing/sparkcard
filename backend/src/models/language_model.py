# sparkcard/backend/src/models/language_model.py
from sqlalchemy import Column, Integer, Text, String
from src.db.base import Base

class Language(Base):
    __tablename__ = 'languages'
    language_id = Column(Integer, primary_key=True)
    language_code = Column(String(10), nullable=False, unique=True)
    language_name = Column(Text, nullable=False)
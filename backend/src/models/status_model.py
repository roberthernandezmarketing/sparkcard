# sparkcard/backend/src/models/status_model.py
from sqlalchemy import Column, Integer, Text
from backend.src.db.base import Base

class Status(Base):
    __tablename__ = 'status'
    status_id = Column(Integer, primary_key=True)
    status_name = Column(Text, nullable=False, unique=True)
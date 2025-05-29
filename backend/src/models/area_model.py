# sparkcard/backend/src/models/area_model.py
from sqlalchemy import Column, Integer, Text
from src.db.base import Base

class Area(Base):
    __tablename__ = 'area'
    area_id = Column(Integer, primary_key=True)
    area_name = Column(Text, nullable=False)
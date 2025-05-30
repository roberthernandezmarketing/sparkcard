# sparkcard/backend/src/models/subarea_model.py
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.src.db.base import Base

class Subarea(Base):
    __tablename__ = 'subarea'
    subarea_id = Column(Integer, primary_key=True)
    subarea_area_id = Column(Integer, ForeignKey('area.area_id'))
    subarea_name = Column(Text, nullable=False)

    area = relationship("Area")
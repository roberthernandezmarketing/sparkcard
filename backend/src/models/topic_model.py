# sparkcard/backend/src/models/topic_model.py
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.src.db.base import Base

class Topic(Base):
    __tablename__ = 'topic'
    topic_id = Column(Integer, primary_key=True)
    topic_subarea_id = Column(Integer, ForeignKey('subarea.subarea_id'))
    topic_name = Column(Text, nullable=False)

    subarea = relationship("Subarea")
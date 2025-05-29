# sparkcard/backend/src/models/subtopic_model.py
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base import Base

class Subtopic(Base):
    __tablename__ = 'subtopic'
    subtopic_id = Column(Integer, primary_key=True)
    subtopic_topic_id = Column(Integer, ForeignKey('topic.topic_id'))
    subtopic_name = Column(Text, nullable=False)

    topic = relationship("Topic")
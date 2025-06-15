#
# sparkcard/backend/src/models/list_model.py
# 
# Defines the list table model, including its columns, data types, primary keys, 
# default values, and relationships to other tables. 
# Defines the list's structure in the database.
# 

from sqlalchemy import Column, String, Text, TIMESTAMP, Integer, ForeignKey, Numeric, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from db.base_class import Base

class List(Base):
    __tablename__ = "lists"

    list_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    list_name = Column(Text, nullable=False)
    list_description = Column(Text)
    list_date_creation = Column(TIMESTAMP, default=datetime.utcnow)
    list_diff_level_id = Column(Integer, ForeignKey("diff_level.diff_level_id", ondelete="CASCADE"))
    list_percent_advanced = Column(Numeric, default=0)
    list_punch_score = Column(Numeric, default=0)
    list_status = Column(String, default='draft')
    list_type = Column(String, default='private')
    list_origin_id = Column(UUID(as_uuid=True), ForeignKey("lists.list_id"))
    list_creator_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    list_xtimes_showed = Column(Integer, default=0)
    list_xtimes_right = Column(Integer, default=0)
    list_xtimes_wrong = Column(Integer, default=0)
    list_xtimes_noanswer = Column(Integer, default=0)
    list_rating_score = Column(Numeric, default=0)
    list_image = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow)

    creator = relationship("User", back_populates="lists")

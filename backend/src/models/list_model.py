#
# sparkcard/backend/src/models/list_model.py
# 
# Defines the list table model, including its columns, data types, primary keys, 
# default values, and relationships to other tables. 
# Defines the list's structure in the database.
# 
from sqlalchemy import Column, String, Text, TIMESTAMP, Integer, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

from backend.src.db.base import Base
# Importa los nuevos modelos de lookup aquí
from backend.src.models.list_status_lookup_model import ListStatusLookup
from backend.src.models.list_type_lookup_model import ListTypeLookup


class List(Base):
    __tablename__ = "lists"

    list_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    list_name = Column(Text, nullable=False)
    list_description = Column(Text)
    list_date_creation = Column(TIMESTAMP, default=datetime.utcnow)
    list_diff_level_id = Column(Integer, ForeignKey("diff_level.diff_level_id", ondelete="CASCADE"))
    list_percent_advanced = Column(Numeric, default=0)
    list_punch_score = Column(Numeric, default=0)
    list_status = Column(Integer, ForeignKey("list_status_lookup.list_status_id", ondelete="RESTRICT")) # Cambiado a RESTRICT para evitar borrar el lookup si hay listas
    list_type = Column(Integer, ForeignKey("list_type_lookup.list_type_id", ondelete="RESTRICT"))       # Cambiado a RESTRICT
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

    # Define las relaciones ORM
    creator = relationship("User", back_populates="lists")
    # Agrega relaciones para los lookups
    status_obj = relationship("ListStatusLookup", backref="lists_with_status") # Puedes renombrar 'status_obj' y 'lists_with_status'
    type_obj = relationship("ListTypeLookup", backref="lists_of_type")         # Puedes renombrar 'type_obj' y 'lists_of_type'


    
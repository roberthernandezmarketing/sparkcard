# 
# backend/src/models/list_type_lookup_model.py
# 
# 
from sqlalchemy import Column, Integer, Text
from backend.src.db.base import Base

class ListTypeLookup(Base):
    __tablename__ = "list_type_lookup"

    list_type_id = Column(Integer, primary_key=True) # Usa 'id' si así lo configuraste en SQL con SERIAL PRIMARY KEY, o 'list_type_id'
    list_type_name = Column(Text, unique=True, nullable=False)
    list_type_description = Column(Text)

    # Opcional: Define una relación inversa si la necesitas
    # lists = relationship("List", back_populates="type") # Necesitarías definir 'type' en el modelo List


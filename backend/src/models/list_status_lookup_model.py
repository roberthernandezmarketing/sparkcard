# 
# backend/src/models/list_status_lookup_model.py
# 
# 
from sqlalchemy import Column, Integer, Text
from backend.src.db.base import Base

class ListStatusLookup(Base):
    __tablename__ = "list_status_lookup"

    list_status_id = Column(Integer, primary_key=True) # Usa 'id' si así lo configuraste en SQL con SERIAL PRIMARY KEY, o 'list_status_id' si prefieres esa convención
    list_status_name = Column(Text, unique=True, nullable=False)
    list_status_description = Column(Text)

    # Opcional: Define una relación inversa si la necesitas
    # lists = relationship("List", back_populates="status") # Necesitarías definir 'status' en el modelo List

    
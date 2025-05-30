# sparkcard/backend/src/models/card_type_model.py
from sqlalchemy import Column, Integer, Text
from backend.src.db.base import Base

class CardType(Base):
    __tablename__ = 'card_type'
    cardtype_id = Column(Integer, primary_key=True)
    cardtype_name = Column(Text, nullable=False, unique=True)
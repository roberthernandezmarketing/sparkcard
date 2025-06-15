# 
# sparkcard/backend/src/services/card_service.py
# 
# Provides a service layer for card-related operations. It contains methods for obtaining, 
# creating, updating, and deleting cards.
# 
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from uuid import UUID  

from backend.src.crud.card_crud import card_crud
from backend.src.schemas.card_schema import CardCreate, CardUpdate
from backend.src.models.card_model import Card as CardModel

class CardService:
    async def get_card_by_id(self, db: AsyncSession, card_id: UUID) -> Optional[CardModel]:
        return await card_crud.get_card(db, card_id)

    async def get_all_cards(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[CardModel]:
        return await card_crud.get_all_cards(db, skip, limit)

    async def create_new_card(self, db: AsyncSession, card_data: CardCreate) -> CardModel:
        return await card_crud.create_card(db, card_data)

    async def update_existing_card(self, db: AsyncSession, card_id: UUID, card_update_data: CardUpdate) -> Optional[CardModel]:
        return await card_crud.update_card(db, card_id, card_update_data)

    async def delete_card_by_id(self, db: AsyncSession, card_id: UUID) -> Optional[CardModel]:
        return await card_crud.delete_card(db, card_id)

card_service = CardService()

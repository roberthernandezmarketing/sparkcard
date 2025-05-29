# sparkcard/backend/src/crud/card.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional

from src.models.card_model   import Card as CardModel
from src.schemas.card_schema import CardCreate, CardUpdate

class CRUDCard:
    async def get_card(self, db: AsyncSession, card_id: int) -> Optional[CardModel]:
        result = await db.execute(select(CardModel).filter(CardModel.card_id == card_id))
        return result.scalar_one_or_none()

    async def get_all_cards(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[CardModel]:
        result = await db.execute(select(CardModel).offset(skip).limit(limit))
        return result.scalars().all()

    async def create_card(self, db: AsyncSession, card: CardCreate) -> CardModel:
        db_card = CardModel(**card.model_dump())
        db.add(db_card)
        await db.commit()
        await db.refresh(db_card)
        return db_card

    async def update_card(self, db: AsyncSession, card_id: int, card_update: CardUpdate) -> Optional[CardModel]:
        db_card = await self.get_card(db, card_id)
        if db_card:
            update_data = card_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_card, key, value)
            await db.commit()
            await db.refresh(db_card)
        return db_card

    async def delete_card(self, db: AsyncSession, card_id: int) -> Optional[CardModel]:
        db_card = await self.get_card(db, card_id)
        if db_card:
            await db.delete(db_card)
            await db.commit()
        return db_card

card_crud = CRUDCard()
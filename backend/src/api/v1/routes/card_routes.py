from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID

from backend.src.schemas.card_schema import Card, CardCreate
from backend.src.services.card_service import card_service
from backend.src.api.v1.deps import get_db_session

router = APIRouter()

@router.get("/", response_model=List[Card])
async def read_cards(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db_session)
):
    """
    Retrieve all cards.
    """
    cards = await card_service.get_all_cards(db, skip=skip, limit=limit)
    return cards

@router.get("/{card_id}", response_model=Card)
async def read_card(
    card_id: UUID,  # Cambiado de int a UUID
    db: AsyncSession = Depends(get_db_session)
):
    """
    Retrieve a single card by ID.
    """
    card = await card_service.get_card_by_id(db, card_id)
    if card is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")
    return card

@router.post("/", response_model=Card, status_code=status.HTTP_201_CREATED)
async def create_card(
    card: CardCreate,
    db: AsyncSession = Depends(get_db_session)
):
    """
    Create a new card.
    """
    created_card = await card_service.create_new_card(db, card)
    return created_card

# Puedes añadir más endpoints para PUT y DELETE si los necesitas más adelante.

# @router.put("/{card_id}", response_model=Card)
# async def update_card_route(
#     card_id: UUID,  # Cambiado de int a UUID
#     card_update: CardUpdate,
#     db: AsyncSession = Depends(get_db_session)
# ):
#     updated_card = await card_service.update_existing_card(db, card_id, card_update)
#     if not updated_card:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")
#     return updated_card

# @router.delete("/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_card_route(
#     card_id: UUID,  # Cambiado de int a UUID
#     db: AsyncSession = Depends(get_db_session)
# ):
#     deleted_card = await card_service.delete_card_by_id(db, card_id)
#     if not deleted_card:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")
#     return {"message": "Card deleted successfully"}

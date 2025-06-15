from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uuid

from backend.src.models.list_model import List
from backend.src.schemas.list_schema import ListCreate, ListUpdate

async def create_list(db: AsyncSession, list_data: ListCreate, user_id: uuid.UUID):
    new_list = List(**list_data.dict(), list_creator_id=user_id)
    db.add(new_list)
    await db.commit()
    await db.refresh(new_list)
    return new_list

async def get_lists_by_user(db: AsyncSession, user_id: uuid.UUID):
    result = await db.execute(select(List).where(List.list_creator_id == user_id))
    return result.scalars().all()

async def get_list_by_id(db: AsyncSession, list_id: uuid.UUID):
    result = await db.execute(select(List).where(List.list_id == list_id))
    return result.scalars().first()

async def update_list(db: AsyncSession, db_list: List, update_data: ListUpdate):
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(db_list, key, value)
    await db.commit()
    await db.refresh(db_list)
    return db_list

async def delete_list(db: AsyncSession, db_list: List):
    await db.delete(db_list)
    await db.commit()

async def get_all_lists(db: AsyncSession):
    result = await db.execute(select(List))
    return result.scalars().all()

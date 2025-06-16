# 
# backend/src/crud/user_crud.py
# 
# Implement CRUD operations for User model, including update and soft delete.
#

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from backend.src.models.user_model import User
from backend.src.schemas.user_schema import UserCreate
from backend.src.utils.security import get_password_hash
import uuid

async def get_user_by_id(db: AsyncSession, user_id: uuid.UUID) -> User | None:
    result = await db.execute(select(User).where(User.user_id == user_id, User.user_is_active == True))
    return result.scalars().first()

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.user_name == username, User.user_is_active == True))
    return result.scalars().first()

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.user_email == email, User.user_is_active == True))
    return result.scalars().first()

async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
    hashed_password = get_password_hash(user_data.user_password_hash)
    new_user = User(
        user_name=user_data.user_name,
        user_email=user_data.user_email,
        user_password_hash=hashed_password,
        user_first_name=user_data.user_first_name,
        user_last_name=user_data.user_last_name,
        user_is_active=True  
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def update_user(db: AsyncSession, user_id: uuid.UUID, updated_data: dict) -> User | None:
    if "user_password_hash" in updated_data:
        updated_data["user_password_hash"] = get_password_hash(updated_data["user_password_hash"])
    stmt = (
        update(User)
        .where(User.user_id == user_id, User.user_is_active == True)
        .values(**updated_data)
        .execution_options(synchronize_session="fetch")
    )
    await db.execute(stmt)
    await db.commit()
    return await get_user_by_id(db, user_id)

async def soft_delete_user(db: AsyncSession, user_id: uuid.UUID) -> bool:
    stmt = (
        update(User)
        .where(User.user_id == user_id)
        .values(user_is_active=False)
        .execution_options(synchronize_session="fetch")
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.rowcount > 0



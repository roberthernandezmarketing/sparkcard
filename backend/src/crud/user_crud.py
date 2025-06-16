# 
# backend/src/crud/user_crud.py
# 
# Implements CRUD operations for the USer model. Handles direct interaction with 
# the Users table in the database.
#
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.src.models.user_model import User
from backend.src.schemas.user_schema import UserCreate
from backend.src.utils.security import get_password_hash
import uuid


async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.user_name == username))
    return result.scalars().first()


async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.user_email == email))
    return result.scalars().first()


async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
    hashed_password = get_password_hash(user_data.user_password_hash)
    new_user = User(
        user_name=user_data.user_name,
        user_email=user_data.user_email,
        user_password_hash=hashed_password,
        user_first_name=user_data.user_first_name,
        user_last_name=user_data.user_last_name,
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_user_by_id(db: AsyncSession, user_id: uuid.UUID):
    result = await db.execute(select(User).where(User.user_id == user_id))
    return result.scalars().first()

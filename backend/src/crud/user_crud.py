# 
# backend/src/crud/user_crud.py
# 
# Implements CRUD operations for the USer model. Handles direct interaction with 
# the Users table in the database.
#
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.src.models.user_model import User
from backend.src.utils.security import get_password_hash

async def create_user(db: AsyncSession, username: str, email: str, password: str):
    hashed_password = get_password_hash(password)
    new_user = User(username=username, email=email, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalars().first()

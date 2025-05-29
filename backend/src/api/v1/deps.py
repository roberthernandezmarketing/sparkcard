# sparkcard/backend/src/api/v1/deps.py
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator # <-- Importa AsyncGenerator
from src.core.database import get_db

# Corrige la anotación de tipo aquí
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get a database session."""
    async for db in get_db():
        yield db
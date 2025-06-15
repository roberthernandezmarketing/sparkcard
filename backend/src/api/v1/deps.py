# 
# sparkcard/backend/src/api/v1/deps.py
# 
# Defines dependencies for injecting a database session (AsyncSession) into API endpoints.
#
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator # <-- Importa AsyncGenerator
from backend.src.core.database import get_db

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get a database session."""
    async for db in get_db():
        yield db
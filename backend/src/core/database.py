# 
# sparkcard/backend/src/core/database.py
# 
# Configure the connection to the PostgreSQL database using SQLAlchemy and asyncio. 
# Define the backend, the asynchronous local session, and a function to retrieve 
# database sessions.
# 
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True) # echo=True para ver las queries SQL en la consola

Base = declarative_base()

# AsyncSessionLocal will be used to create session instances
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False, # Important for async sessions
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
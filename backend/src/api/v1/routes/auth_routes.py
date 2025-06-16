# 
# backend/src/api/v1/routes/auth_routes.py
# 
# Defines the API endpoints related to users (CRUD: Create, Read, Update, Delete).
# 
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from backend.src.schemas.user_schema import UserCreate, UserOut, Token
from backend.src.crud.user_crud import create_user, get_user_by_username
from backend.src.utils.security import verify_password, create_access_token
from backend.src.core.database import get_db

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_username(db, user_data.user_name)  # use user_name of Model
    if user:
        raise HTTPException(status_code=400, detail="The user already exists")
    new_user = await create_user(db, user_data)
    return new_user

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await get_user_by_username(db, form_data.username)  # use username in form
    if not user or not verify_password(form_data.password, user.user_password_hash):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": str(user.user_name)})
    return {"access_token": access_token, "token_type": "bearer"}

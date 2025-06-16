# 
# backend/src/api/v1/routes/auth_routes.py
# 
# Defines the API endpoints related to users (CRUD: Create, Read, Update, Delete).
# 
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.ext.asyncio import AsyncSession
from backend.src.schemas.user_schema import UserCreate, UserOut, Token
from backend.src.crud.user_crud import create_user, get_user_by_username, update_user, soft_delete_user, get_user_by_id
from backend.src.utils.security import verify_password, create_access_token
from backend.src.core.database import get_db
from backend.src.api.v1.deps_user import get_current_user
import uuid

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

@router.get("/me", response_model=UserOut)
async def get_me(current_user: UserOut = Depends(get_current_user)):
    return current_user

@router.put("/users/{user_id}", response_model=UserOut)
async def update_user_route(
    user_id: uuid.UUID,
    updated_user: UserCreate = Body(...),
    current_user: UserOut = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    # Solo el usuario mismo o un admin podrían modificar (luego agregar roles)
    if current_user.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this user")
    updated_data = updated_user.dict(exclude_unset=True)
    updated = await update_user(db, user_id, updated_data)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_route(
    user_id: uuid.UUID,
    current_user: UserOut = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    # Igual que arriba, validar permisos
    if current_user.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this user")
    deleted = await soft_delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found or already deleted")
    return None
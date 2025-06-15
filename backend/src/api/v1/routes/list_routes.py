from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID

from backend.src.api.v1.deps import get_db_session
from backend.src.schemas.list_schema import ListCreate, ListUpdate, ListOut
from backend.src.crud import list_crud
# from backend.src.utils.auth import get_current_user
# from backend.src.models.user_model import User

router = APIRouter(prefix="/lists", tags=["Lists"])

# 🟢 Sin autenticación por ahora

@router.get("/all", response_model=List[ListOut])
async def get_all_lists(
    db: AsyncSession = Depends(get_db_session),
):
    return await list_crud.get_all_lists(db)

@router.post("/", response_model=ListOut)
async def create_list(
    list_data: ListCreate,
    db: AsyncSession = Depends(get_db_session),
    # current_user: User = Depends(get_current_user)
):
    # return await list_crud.create_list(db, list_data, current_user.user_id)
    return await list_crud.create_list(db, list_data, user_id=None)

@router.get("/{list_id}", response_model=ListOut)
async def get_list_by_id(
    list_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    # current_user: User = Depends(get_current_user)
):
    db_list = await list_crud.get_list_by_id(db, list_id)
    if not db_list:
        raise HTTPException(status_code=404, detail="List not found")
    return db_list

@router.put("/{list_id}", response_model=ListOut)
async def update_list(
    list_id: UUID,
    list_data: ListUpdate,
    db: AsyncSession = Depends(get_db_session),
    # current_user: User = Depends(get_current_user)
):
    db_list = await list_crud.get_list_by_id(db, list_id)
    if not db_list:
        raise HTTPException(status_code=404, detail="List not found")
    return await list_crud.update_list(db, db_list, list_data)

@router.delete("/{list_id}")
async def delete_list(
    list_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    # current_user: User = Depends(get_current_user)
):
    db_list = await list_crud.get_list_by_id(db, list_id)
    if not db_list:
        raise HTTPException(status_code=404, detail="List not found")
    await list_crud.delete_list(db, db_list)
    return {"msg": "List deleted"}

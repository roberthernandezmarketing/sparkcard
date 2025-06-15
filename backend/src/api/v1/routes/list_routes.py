# 
# sparkcard/backend/src/api/v1/routes/list_routes.py
# 
# Defines the API endpoints related to list (CRUD: Create, Read, Update, Delete).
# 
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid
from typing import List

from backend.src.core.database import get_db
from backend.src.schemas.list_schema import ListCreate, ListUpdate, ListOut
# from backend.src.crud import list as crud_list
from backend.src.crud import list_crud as crud_list
from backend.src.utils.auth import get_current_user
from backend.src.models.user_model import User

router = APIRouter(prefix="/lists", tags=["Lists"])

@router.post("/", response_model=ListOut)
def create_list(
    list_data: ListCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_list.create_list(db, list_data, current_user.user_id)

@router.get("/", response_model=List[ListOut])
def get_my_lists(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_list.get_lists_by_user(db, current_user.user_id)

@router.get("/{list_id}", response_model=ListOut)
def get_list_by_id(
    list_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_list = crud_list.get_list_by_id(db, list_id)
    if not db_list:
        raise HTTPException(status_code=404, detail="List not found")
    return db_list

@router.put("/{list_id}", response_model=ListOut)
def update_list(
    list_id: uuid.UUID,
    list_data: ListUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_list = crud_list.get_list_by_id(db, list_id)
    if not db_list:
        raise HTTPException(status_code=404, detail="List not found")
    return crud_list.update_list(db, db_list, list_data)

@router.delete("/{list_id}")
def delete_list(
    list_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_list = crud_list.get_list_by_id(db, list_id)
    if not db_list:
        raise HTTPException(status_code=404, detail="List not found")
    crud_list.delete_list(db, db_list)
    return {"msg": "List deleted"}

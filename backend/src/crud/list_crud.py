# 
# sparkcard/backend/src/crud/list_crud.py
# 
# Implements CRUD operations for the List model. Handles direct interaction with 
# the List table in the database.
# 
from sqlalchemy.orm import Session
import uuid

from backend.src.models.list_model import List
from backend.src.schemas.list_schema import ListCreate, ListUpdate

def create_list(db: Session, list_data: ListCreate, user_id: uuid.UUID):
    new_list = List(**list_data.dict(), list_creator_id=user_id)
    db.add(new_list)
    db.commit()
    db.refresh(new_list)
    return new_list

def get_lists_by_user(db: Session, user_id: uuid.UUID):
    return db.query(List).filter(List.list_creator_id == user_id).all()

def get_list_by_id(db: Session, list_id: uuid.UUID):
    return db.query(List).filter(List.list_id == list_id).first()

def update_list(db: Session, db_list: List, update_data: ListUpdate):
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(db_list, key, value)
    db.commit()
    db.refresh(db_list)
    return db_list

def delete_list(db: Session, db_list: List):
    db.delete(db_list)
    db.commit()

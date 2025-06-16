# 
# backend/src/schemas/user_schema.py
# 
# Defines the Pydantic schemas for login (UserLogin), create (UserCreate), 
# It includes type validation and field optionality. 
# 
from pydantic import BaseModel, EmailStr
import uuid

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    user_id: uuid.UUID
    username: str
    email: EmailStr

    class Config:
    # orm_mode = True   # from Pydantic V1 to V2
      from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

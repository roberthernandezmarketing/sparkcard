# 
# backend/src/schemas/user_schema.py
# 
# Defines the Pydantic schemas for login (UserLogin), create (UserCreate), 
# It includes type validation and field optionality. 
# 
from pydantic import BaseModel, EmailStr, Field
import uuid

class UserCreate(BaseModel):
    user_name: str
    user_email: EmailStr
    user_password_hash: str
    user_first_name: str
    user_last_name: str

class UserOut(BaseModel):
    user_id: uuid.UUID
    user_name: str
    user_email: EmailStr
    user_first_name: str
    user_last_name: str

    class Config:
    # orm_mode = True   # from Pydantic V1 to V2
      from_attributes = True

class UserLogin(BaseModel):
    user_name: str
    user_password_hash: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ChangePasswordRequest(BaseModel):
    current_password: str = Field(..., min_length=6)
    new_password: str = Field(..., min_length=6)
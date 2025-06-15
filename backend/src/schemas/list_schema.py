#
# sparkcard/backend/src/services/list_schema.py
# 
# Defines the Pydantic schemas for creating (ListCreate),  
# It includes type validation and field optionality. 
# 
from pydantic import BaseModel, UUID4, Field
from typing import Optional
from datetime import datetime

class ListBase(BaseModel):
    list_name: str
    list_description: Optional[str] = None
    list_diff_level_id: Optional[int] = None
    list_type: Optional[int] = 2
    list_status: Optional[int] = 1
    list_image: Optional[str] = None
    list_origin_id: Optional[UUID4] = None

class ListCreate(ListBase):
    pass

class ListUpdate(ListBase):
    pass

class ListOut(ListBase):
    list_id: UUID4
    list_percent_advanced: float
    list_punch_score: float
    list_rating_score: float
    created_at: datetime
    updated_at: datetime

    class Config:
        # orm_mode = True   # from Pydantic V1 to V2
        from_attributes = True

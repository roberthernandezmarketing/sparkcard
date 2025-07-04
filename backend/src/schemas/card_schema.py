#
# sparkcard/backend/src/services/card_service.py
# 
# Defines the Pydantic schemas for creating (CardCreate), updating (CardUpdate), 
# and reading (Card). It includes type validation and field optionality. 
# 
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import UUID

# Base Schema for Card creation/update
class CardBase(BaseModel):
    card_area_id: int
    card_subarea_id: int
    card_topic_id: int
    card_subtopic_id: int
    card_language_id: int
    card_source_id: int
    card_type_id: int
    card_diff_level_id: int
    card_question_concept: str
    card_question_type_id: int
    card_answer_options: List[str] = Field(default_factory=list)
    card_correct_answers: List[str] = Field(default_factory=list)
    card_explanation: Optional[str] = None
    card_creator_id: UUID 
    card_status_id: int

# Schema for creating a Card
class CardCreate(CardBase):
    pass

# Schema for updating a Card (all fields are optional)
class CardUpdate(BaseModel):
    card_area_id: Optional[int] = None
    card_subarea_id: Optional[int] = None
    card_topic_id: Optional[int] = None
    card_subtopic_id: Optional[int] = None
    card_language_id: Optional[int] = None
    card_source_id: Optional[int] = None
    card_type_id: Optional[int] = None
    card_diff_level_id: Optional[int] = None
    card_question_concept: Optional[str] = None
    card_question_type_id: Optional[int] = None
    card_answer_options: Optional[List[str]] = None
    card_correct_answers: Optional[List[str]] = None
    card_explanation: Optional[str] = None
    card_creator_id: Optional[UUID] = None  
    card_status_id: Optional[int] = None

# Schema for reading a Card (includes ID and default values)
class Card(CardBase):
    card_id: UUID  
    card_date_creation: datetime
    card_xtimes_showed: int
    card_xtimes_right: int
    card_xtimes_wrong: int
    card_xtimes_noanswer: int
    card_xtimes_inlist: int
    card_rating_score: int

    class Config:
        from_attributes = True

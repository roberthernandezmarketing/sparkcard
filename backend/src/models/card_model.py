from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, Boolean, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import uuid4
from backend.src.db.base import Base

class Card(Base):
    __tablename__ = 'card'
    card_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    card_area_id = Column(Integer, ForeignKey('area.area_id', ondelete='CASCADE'))
    card_subarea_id = Column(Integer, ForeignKey('subarea.subarea_id', ondelete='CASCADE'))
    card_topic_id = Column(Integer, ForeignKey('topic.topic_id', ondelete='CASCADE'))
    card_subtopic_id = Column(Integer, ForeignKey('subtopic.subtopic_id', ondelete='CASCADE'))
    card_language_id = Column(Integer, ForeignKey('languages.language_id', ondelete='CASCADE'))
    card_source_id = Column(Integer, ForeignKey('sources.sources_id', ondelete='CASCADE'))
    card_type_id = Column(Integer, ForeignKey('card_type.cardtype_id', ondelete='CASCADE'))
    card_diff_level_id = Column(Integer, ForeignKey('diff_level.diff_level_id', ondelete='CASCADE'))
    
    card_question_concept = Column(Text)
    card_question_type_id = Column(Integer, ForeignKey('question_type.question_type_id', ondelete='CASCADE'))
    card_answer_options = Column(ARRAY(Text)) # Stores a list of strings
    card_correct_answers = Column(ARRAY(Text)) # Stores a list of strings
    card_explanation = Column(Text)
    
    card_creator_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id', ondelete='CASCADE'))
    card_status_id = Column(Integer, ForeignKey('status.status_id', ondelete='CASCADE'))
    card_date_creation = Column(TIMESTAMP(timezone=True), default=datetime.now)
    
    card_xtimes_showed = Column(Integer, default=0)
    card_xtimes_right = Column(Integer, default=0)
    card_xtimes_wrong = Column(Integer, default=0)
    card_xtimes_noanswer = Column(Integer, default=0)
    card_xtimes_inlist = Column(Integer, default=0)
    card_rating_score = Column(Integer, default=0)

    # Relationships
    area = relationship("Area")
    subarea = relationship("Subarea")
    topic = relationship("Topic")
    subtopic = relationship("Subtopic")
    language = relationship("Language")
    source = relationship("Source")
    card_type = relationship("CardType")
    difficulty_level = relationship("DifficultyLevel")
    question_type = relationship("QuestionType")
    creator = relationship("User")
    status = relationship("Status")

class Tag(Base):
    __tablename__ = 'tags'
    tags_id = Column(Integer, primary_key=True)
    tags_name = Column(Text, nullable=False, unique=True)

class CardTag(Base):
    __tablename__ = 'card_tags'
    card_id = Column(Integer, ForeignKey('card.card_id', ondelete='CASCADE'), primary_key=True)
    tags_id = Column(Integer, ForeignKey('tags.tags_id', ondelete='CASCADE'), primary_key=True)

class Keyword(Base):
    __tablename__ = 'keywords'
    keywords_id = Column(Integer, primary_key=True)
    keywords_name = Column(Text, nullable=False, unique=True)

class CardKeyword(Base):
    __tablename__ = 'card_keywords'
    card_id = Column(Integer, ForeignKey('card.card_id', ondelete='CASCADE'), primary_key=True)
    keywords_id = Column(Integer, ForeignKey('keywords.keywords_id', ondelete='CASCADE'), primary_key=True)

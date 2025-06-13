from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from backend.src.db.base import Base

class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    author_name = Column(Text, nullable=False, unique=True)

class Editorial(Base):
    __tablename__ = 'editorials'
    editorial_id = Column(Integer, primary_key=True)
    editorial_name = Column(Text, nullable=False, unique=True)

class SourceChannel(Base):
    __tablename__ = 'source_channel'
    source_channel_id = Column(Integer, primary_key=True)
    source_channel_name = Column(Text, nullable=False, unique=True)

class Source(Base):
    __tablename__ = 'sources'
    sources_id = Column(Integer, primary_key=True)
    sources_title = Column(Text, nullable=False)
    sources_author_id = Column(UUID(as_uuid=True), ForeignKey('authors.author_id'))
    sources_edition = Column(Text)
    sources_year = Column(Integer)
    sources_editorial_id = Column(Integer, ForeignKey('editorials.editorial_id'))
    sources_pages = Column(Text)
    sources_isbn = Column(String(20), unique=True)
    sources_channel_id = Column(Integer, ForeignKey('source_channel.source_channel_id'))
    sources_url = Column(Text)
    sources_area_id = Column(Integer, ForeignKey('area.area_id'))

    author = relationship("Author")
    editorial = relationship("Editorial")
    channel = relationship("SourceChannel")

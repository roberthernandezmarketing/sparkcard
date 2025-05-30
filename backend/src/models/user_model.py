# sparkcard/backend/src/models/user_model.py
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.src.db.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=True, nullable=False)
    user_email = Column(String(255), unique=True)
    user_password_hash = Column(String(255), nullable=False)
    user_first_name = Column(String(100))
    user_last_name = Column(String(100))
    user_registration_date = Column(TIMESTAMP(timezone=True), default=datetime.now)
    user_is_active = Column(Boolean, default=True)

class Role(Base):
    __tablename__ = 'roles'
    role_id = Column(Integer, primary_key=True)
    role_name = Column(String(50), unique=True, nullable=False)

class UserRole(Base):
    __tablename__ = 'user_roles'
    user_roles_user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), primary_key=True)
    user_roles_role_id = Column(Integer, ForeignKey('roles.role_id', ondelete='CASCADE'), primary_key=True)

    user = relationship("User")
    role = relationship("Role")
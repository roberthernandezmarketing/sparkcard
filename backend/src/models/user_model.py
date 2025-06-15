# 
# backend/src/models/user_model.py
# 
# Es un archivo que define las clases Python que representan las tablas users, roles y 
# user_roles de tu base de datos. Estas clases se llaman modelos SQLAlchemy, y permiten:
# Crear tablas automáticamente en la DB (si usas Alembic o .create_all()).
# Interactuar con los registros como objetos Python (crear, leer, actualizar, borrar).
# Definir relaciones entre entidades (por ejemplo, un usuario tiene muchas listas).
# 

from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import uuid4

from backend.src.db.base import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_name = Column(String(50), unique=True, nullable=False)
    user_email = Column(String(255), unique=True)
    user_password_hash = Column(String(255), nullable=False)
    user_first_name = Column(String(100))
    user_last_name = Column(String(100))
    user_registration_date = Column(TIMESTAMP(timezone=True), default=datetime.now)
    user_is_active = Column(Boolean, default=True)

    # Relación con las listas creadas por el usuario
    lists = relationship("List", back_populates="creator", cascade="all, delete-orphan")


class Role(Base):
    __tablename__ = 'roles'

    role_id = Column(Integer, primary_key=True)
    role_name = Column(String(50), unique=True, nullable=False)


class UserRole(Base):
    __tablename__ = 'user_roles'

    user_roles_user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id', ondelete='CASCADE'), primary_key=True)
    user_roles_role_id = Column(Integer, ForeignKey('roles.role_id', ondelete='CASCADE'), primary_key=True)

    user = relationship("User")
    role = relationship("Role")


# IMPORTACIÓN TARDÍA PARA EVITAR IMPORT CIRCULAR
from backend.src.models.list_model import List

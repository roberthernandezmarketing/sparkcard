# sparkcard/backend/src/utils/auth.py

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid

from backend.src.core.database import get_db
from backend.src.models.user_model import User

# Dummy user para pruebas (puedes sustituir por lógica real luego)
def get_current_user(db: Session = Depends(get_db)) -> User:
    # Aquí deberías colocar la lógica real con JWT/OAuth2
    # Por ahora solo devuelve un usuario ficticio o lanza error si quieres simular auth fallida

    # 🟢 OPCIÓN 1: Usuario dummy fijo para pruebas (puedes cambiar el UUID por uno real de tu DB)
    dummy_user = User(
        user_id=uuid.UUID("11111111-1111-1111-1111-111111111111"),
        user_name="test_user",
        user_email="test@example.com",
        user_hashed_password="not_relevant",
    )
    return dummy_user

    # 🔴 OPCIÓN 2: Lanzar error para simular "no autenticado"
    # raise HTTPException(
    #     status_code=status.HTTP_401_UNAUTHORIZED,
    #     detail="Not authenticated",
    #     headers={"WWW-Authenticate": "Bearer"},
    # )

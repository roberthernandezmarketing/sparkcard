# 
# sparkcard/backend/src/api/v1/deps_user.py
# 
# Defines dependencies for retrieving the currently authenticated user using JWT.
#
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from backend.src.core.database import get_db
from backend.src.schemas.user_schema import UserOut
from backend.src.crud.user_crud import get_user_by_username
from sqlalchemy.ext.asyncio import AsyncSession
import os

SECRET_KEY = os.getenv("SECRET_KEY", "fallback_dev_key_unsafe")
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)) -> UserOut:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token: no subject")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate token")

    user = await get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user

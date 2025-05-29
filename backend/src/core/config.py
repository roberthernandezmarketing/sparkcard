# 
# sparkcard/backend/src/core/config.py
# 
# configuración general de la aplicación y la conexión a la base de datos.
# 
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv() # Cargar variables de entorno del archivo .env

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
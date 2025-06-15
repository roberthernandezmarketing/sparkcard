# 
# sparkcard/backend/src/core/config.py
# 
# Handles application configuration, loading environment variables (such as DATABASE_URL) 
# from a .env file using Pydantic-settings.
# 
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from the .env file

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
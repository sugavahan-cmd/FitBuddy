import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# This line explicitly forces the system to read your .env file
load_dotenv()

class Settings(BaseSettings):
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_WORKOUT_MODEL: str = os.getenv("GEMINI_WORKOUT_MODEL", "gemini-2.5-flash")
    GEMINI_TIP_MODEL: str = os.getenv("GEMINI_TIP_MODEL", "gemini-2.5-flash")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./fitbuddy.db")
    ADMIN_TOKEN: str = os.getenv("ADMIN_TOKEN", "fitbuddy-admin")
    APP_NAME: str = os.getenv("APP_NAME", "FitBuddy")

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
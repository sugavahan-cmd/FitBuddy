from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router

app = FastAPI(
    title="FitBuddy - AI Fitness Plan Generator",
    description="Intelligent 7-day fitness routine and nutrition planner powered by Google Gemini.",
    version="1.0.0"
)

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
app.include_router(router)
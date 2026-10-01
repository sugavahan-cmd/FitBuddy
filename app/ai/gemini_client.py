import google.generativeai as genai
from app.config import settings

def init_gemini() -> None:
    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable is missing.")
    genai.configure(api_key=settings.GEMINI_API_KEY)

def get_gemini_pro_model() -> genai.GenerativeModel:
    init_gemini()
    return genai.GenerativeModel(settings.GEMINI_WORKOUT_MODEL)

def get_gemini_flash_model() -> genai.GenerativeModel:
    init_gemini()
    return genai.GenerativeModel(settings.GEMINI_TIP_MODEL)
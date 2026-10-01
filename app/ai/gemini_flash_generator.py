from app.ai.gemini_client import get_gemini_flash_model

def generate_nutrition_tip_with_flash(goal: str) -> str:
    model = get_gemini_flash_model()
    prompt = f"""
You are a sports nutritionist. Deliver a single, high-impact, practical nutrition or recovery guideline for an individual pursuing the fitness goal: '{goal}'.
Focus on specific protein intake recommendations, hydration strategies, or recovery timing. Keep it concise, engaging, and directly applicable.
"""
    response = model.generate_content(prompt)
    return response.text.strip()
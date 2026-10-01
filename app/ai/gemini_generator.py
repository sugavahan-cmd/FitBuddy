from app.ai.gemini_client import get_gemini_pro_model

def generate_workout_gemini(goal: str, intensity: str) -> str:
    model = get_gemini_pro_model()
    prompt = f"""
You are an elite certified personal fitness trainer.
Generate a structured, professional 7-Day Workout Routine tailored to the following user parameters:
- Fitness Goal: {goal}
- Preferred Intensity: {intensity}

For each day (Day 1 through Day 7), include:
1. Focus Area (e.g., Upper Body Strength, Cardio & Core, Active Recovery)
2. Warm-up (5-10 minutes with exercise names and durations)
3. Main Workout (curated exercises with targeted sets, rep ranges, and rest intervals)
4. Cooldown & Mobility (stretching or breathing)

Ensure clean, legible plaintext formatting without excessive markdown symbols.
"""
    response = model.generate_content(prompt)
    return response.text.strip()
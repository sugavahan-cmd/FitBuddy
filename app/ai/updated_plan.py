from app.ai.gemini_client import get_gemini_pro_model

def update_workout_plan(original_plan: str, feedback: str) -> str:
    model = get_gemini_pro_model()
    prompt = f"""
You are an expert fitness coach revising a client's workout plan.
Below is the client's current 7-Day Workout Plan:
---
{original_plan}
---

The client has submitted this specific feedback:
"{feedback}"

Update and rebalance the 7-day routine by directly implementing this feedback while preserving overall training safety, progression, and structure.
Return the complete revised 7-day routine in clear, structured plaintext.
"""
    response = model.generate_content(prompt)
    return response.text.strip()
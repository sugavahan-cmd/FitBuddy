def get_basic_nutrition_guidelines(goal: str) -> str:
    goal_lower = goal.lower()
    if goal_lower == "weight loss":
        return "Maintain a healthy caloric deficit and prioritize high-protein meals."
    elif goal_lower == "muscle gain":
        return "Maintain a caloric surplus and consume 1.6g to 2.2g of protein per kg of body weight."
    return "Maintain a balanced diet rich in whole foods, vegetables, and lean proteins."
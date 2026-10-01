from pathlib import Path
from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db, UserRecord
from app.ai.gemini_generator import generate_workout_gemini
from app.ai.gemini_flash_generator import generate_nutrition_tip_with_flash
from app.ai.updated_plan import update_workout_plan

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )

@router.post("/generate-workout")
def generate_workout(
    request: Request,
    username: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: int = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        workout_plan = generate_workout_gemini(goal, intensity)
        nutrition_tip = generate_nutrition_tip_with_flash(goal)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI generation failed: {str(e)}")

    existing_user = db.query(UserRecord).filter(UserRecord.user_id == user_id).first()
    if existing_user:
        existing_user.username = username
        existing_user.age = age
        existing_user.weight = weight
        existing_user.goal = goal
        existing_user.intensity = intensity
        existing_user.original_plan = workout_plan
        existing_user.updated_plan = None
    else:
        new_user = UserRecord(
            user_id=user_id,
            username=username,
            age=age,
            weight=weight,
            goal=goal,
            intensity=intensity,
            original_plan=workout_plan,
            updated_plan=None
        )
        db.add(new_user)

    db.commit()

    return templates.TemplateResponse(
        request=request, 
        name="result.html", 
        context={
            "username": username,
            "user_id": user_id,
            "age": age,
            "weight": weight,
            "goal": goal,
            "intensity": intensity,
            "workout_plan": workout_plan,
            "nutrition_tip": nutrition_tip,
            "is_updated": False
        }
    )

@router.post("/submit-feedback")
def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(UserRecord).filter(UserRecord.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User record not found.")

    base_plan = user.updated_plan if user.updated_plan else user.original_plan
    try:
        revised_plan = update_workout_plan(base_plan, feedback)
        nutrition_tip = generate_nutrition_tip_with_flash(user.goal)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Feedback revision failed: {str(e)}")

    user.updated_plan = revised_plan
    db.commit()

    return templates.TemplateResponse(
        request=request, 
        name="result.html", 
        context={
            "username": user.username,
            "user_id": user.user_id,
            "age": user.age,
            "weight": user.weight,
            "goal": user.goal,
            "intensity": user.intensity,
            "workout_plan": revised_plan,
            "nutrition_tip": nutrition_tip,
            "is_updated": True
        }
    )

@router.get("/view-all-users")
def view_all_users(request: Request, db: Session = Depends(get_db)):
    users = db.query(UserRecord).order_by(UserRecord.id.desc()).all()
    return templates.TemplateResponse(
        request=request, 
        name="all_users.html", 
        context={
            "users": users
        }
    )
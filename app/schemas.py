from pydantic import BaseModel, Field
from typing import Optional

class UserInput(BaseModel):
    username: str = Field(..., min_length=2, max_length=50)
    user_id: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=12, le=100)
    weight: int = Field(..., ge=30, le=250)
    goal: str = Field(...)
    intensity: str = Field(...)

class FeedbackRequest(BaseModel):
    user_id: str = Field(...)
    feedback: str = Field(..., min_length=3, max_length=1000)

class UserResponse(BaseModel):
    id: int
    user_id: str
    username: str
    age: int
    weight: int
    goal: str
    intensity: str
    original_plan: Optional[str] = None
    updated_plan: Optional[str] = None

    class Config:
        from_attributes = True
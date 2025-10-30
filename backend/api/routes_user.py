from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class UserOut(BaseModel):
    id: int
    email: str


@router.get("/", response_model=List[UserOut])
async def list_users():
    """Return a small list of users (mock)."""
    return [{"id": 1, "email": "demo@example.com"}]


@router.get("/me", response_model=UserOut)
async def get_me():
    """Return the current (mock) user."""
    return {"id": 1, "email": "demo@example.com"}

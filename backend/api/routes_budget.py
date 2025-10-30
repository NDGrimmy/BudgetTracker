from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class BudgetOut(BaseModel):
    id: int
    name: str
    target: float
    progress: float


@router.get("/", response_model=List[BudgetOut])
async def list_budgets():
    """Return mock budget summaries."""
    return [
        {"id": 1, "name": "Groceries", "target": 400.0, "progress": 125.5},
        {"id": 2, "name": "Entertainment", "target": 200.0, "progress": 50.0},
    ]


@router.get("/{budget_id}", response_model=BudgetOut)
async def get_budget(budget_id: int):
    return {"id": budget_id, "name": "Sample", "target": 100.0, "progress": 10.0}

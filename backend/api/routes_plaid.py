from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from datetime import date

router = APIRouter()


class PlaidExchangeIn(BaseModel):
    public_token: str


class TransactionOut(BaseModel):
    id: str
    date: date
    name: str
    amount: float
    category: List[str] | None = None


@router.post("/exchange")
async def exchange_token(payload: PlaidExchangeIn):
    """Mock exchange of a public token for an access token."""
    return {"access_token": "sandbox-access-token", "item_id": "sandbox-item"}


@router.get("/transactions", response_model=List[TransactionOut])
async def list_transactions():
    """Return a few mocked transactions."""
    return [
        {"id": "t1", "date": date.today().isoformat(), "name": "Coffee Shop", "amount": 4.5, "category": ["Food", "Coffee"]},
        {"id": "t2", "date": date.today().isoformat(), "name": "Grocery Store", "amount": 64.12, "category": ["Food", "Groceries"]},
    ]

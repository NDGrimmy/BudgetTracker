"""Minimal stub of a Plaid integration service (sandbox/mock).

This file provides small helpers that other parts of the app can call.
"""
from typing import List
from datetime import date


def exchange_public_token(public_token: str) -> dict:
    # In a real implementation this would call Plaid's /item/public_token/exchange
    return {"access_token": "sandbox-access-token", "item_id": "sandbox-item"}


def fetch_transactions(access_token: str, start_date: date, end_date: date) -> List[dict]:
    # Return a few mock transactions for local development
    return [
        {"id": "txn_1", "date": start_date.isoformat(), "name": "Coffee", "amount": 3.5, "category": ["Food", "Coffee"]},
        {"id": "txn_2", "date": end_date.isoformat(), "name": "Bookstore", "amount": 24.99, "category": ["Shopping", "Books"]},
    ]

from typing import Optional


def get_user_by_id(user_id: int) -> Optional[dict]:
    # placeholder for a real DB lookup
    if user_id == 1:
        return {"id": 1, "email": "demo@example.com"}
    return None

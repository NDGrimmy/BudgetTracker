from typing import Optional


def create_access_token(data: dict) -> str:
    """Stub: create a JWT access token for a user. Replace with real implementation."""
    # In a real app use `python-jose` or `pyjwt` and sign with JWT_SECRET
    return "token-please-replace"


def verify_token(token: str) -> Optional[dict]:
    """Stub: verify a token and return the payload or None."""
    if token == "token-please-replace":
        return {"sub": "1"}
    return None

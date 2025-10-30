import os
from dotenv import load_dotenv

load_dotenv()

PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")
PLAID_ENV = os.getenv("PLAID_ENV", "sandbox")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

JWT_SECRET = os.getenv("JWT_SECRET", "please-change-me")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

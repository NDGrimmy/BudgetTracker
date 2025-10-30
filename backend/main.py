from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes_user import router as user_router
from api.routes_budget import router as budget_router
from api.routes_plaid import router as plaid_router

app = FastAPI(title="BudgetTracker - Backend", version="0.1.0")

# Basic CORS for local frontend development
origins = ["http://localhost", "http://localhost:5173", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", summary="Root")
async def read_root():
    return {"message": "Hello, World!", "service": "BudgetTracker Backend"}


@app.get("/health", summary="Health check")
async def health_check():
    return {"status": "ok"}


# Register routers
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(budget_router, prefix="/budgets", tags=["budgets"])
app.include_router(plaid_router, prefix="/plaid", tags=["plaid"])

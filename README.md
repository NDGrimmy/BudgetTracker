# BudgetTracker
BudgetTracker is a personal finance dashboard that connects to the Plaid API (sandbox mode) to fetch and categorize transaction data.  
It visualizes spending trends, budgets, and categories in an interactive, full-stack web application.

This project demonstrates modern backend architecture, containerized deployment, API integration, and frontend visualization — all while remaining fully free to develop and run locally.

---

## Overview

BudgetTracker is built as a modular full-stack application with a FastAPI backend and React frontend.  
It integrates with the Plaid sandbox to simulate financial data securely, without requiring any real bank accounts or paid environments.

The goal is to create a developer-ready, production-style finance tracker that highlights end-to-end understanding of web systems, API security, and scalable design.

---

## Features

- Secure Plaid sandbox integration for mock bank data
- Transaction fetching, storage, and categorization
- User authentication and session management (JWT)
- Budget goal creation and progress tracking
- Dynamic data visualization (monthly trends, category breakdowns)
- Modular, containerized architecture for local development
- Ready for Kubernetes deployment (Helm chart optional)

---

## Tech Stack

### Backend
- **Language:** Python 3.13
- **Framework:** FastAPI
- **Package Manager:** [UV](https://github.com/astral-sh/uv)
- **Database:** PostgreSQL
- **Cache / Task Queue:** Redis
- **ORM:** SQLAlchemy
- **Auth:** JWT (JSON Web Tokens)
- **Asynchronous Jobs:** Celery (optional)
- **Testing:** pytest
- **Docs:** Auto-generated with OpenAPI (via FastAPI)

### Frontend
- **Framework:** React (Vite)
- **Styling:** Tailwind CSS
- **Charts:** Recharts or Plotly
- **Build Tool:** Vite
- **API Integration:** Axios / Fetch API

### Infrastructure
- **Containers:** Docker + Docker Compose
- **Proxy:** Nginx reverse proxy
- **Environment:** Local development, optional Kubernetes (Minikube or K3s)
- **CI/CD:** GitHub Actions
- **Monitoring (optional):** Prometheus + Grafana

### External Integrations
- **Plaid Sandbox API** – for transaction data simulation  
  Documentation: [https://plaid.com/docs/sandbox](https://plaid.com/docs/sandbox)

---

## Project Structure

```
BudgetTracker/
├── backend/
│ ├── main.py # FastAPI entry point
│ ├── api/ # API routes
│ │ ├── routes_user.py
│ │ ├── routes_budget.py
│ │ └── routes_plaid.py
│ ├── models/ # SQLAlchemy models
│ │ ├── user.py
│ │ └── transaction.py
│ ├── services/ # Core logic and integrations
│ │ ├── plaid_service.py
│ │ ├── budget_service.py
│ │ └── user_service.py
│ └── utils/ # Helpers, config, caching
│ ├── auth.py
│ ├── config.py
│ └── database.py
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ ├── hooks/
│ │ └── api/
│ ├── vite.config.js
│ └── package.json
│
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
├── .env.example
└── README.md
```

---

## Environment Variables
```
Create a `.env` file in the project root with the following keys:

PLAID_CLIENT_ID=your_client_id
PLAID_SECRET=your_sandbox_secret
PLAID_ENV=sandbox

DATABASE_URL=postgresql://user:password@db:5432/BudgetTracker
REDIS_URL=redis://redis:6379/0

JWT_SECRET=your_jwt_secret_key
JWT_ALGORITHM=HS256
```

Plaid credentials for the sandbox can be obtained from the Plaid dashboard after creating a free account.

---

## Running Locally

### Requirements
- Docker
- Docker Compose
- UV (Python package manager)
- Node.js 18+ (for frontend)

### Backend Setup

```
cd backend
uv venv
uv sync
uv run uvicorn main:app --reload
```

This will create a virtual environment, install dependencies, and start the FastAPI development server.

Frontend Setup
```
cd frontend
npm install
npm run dev
The frontend will run at http://localhost:5173 and connect to the backend API.
```

Full Stack (Docker Compose)
From the project root:

```
docker-compose up --build
```

This starts:

FastAPI backend

React frontend

PostgreSQL database

Redis cache

Nginx reverse proxy

Access the app at http://localhost:8080.

Testing
Run backend tests:

```
cd backend
uv run pytest
```

Tests should cover models, API routes, and Plaid service integrations.

Future Work
User-configurable categories

Machine learning categorization of transactions

Kubernetes Helm deployment

CI/CD with GitHub Actions

OAuth-based Plaid integration for production use

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import analytics, config, developer, health

app = FastAPI(
    title="CogniStream API",
    description="Developer Flow-State & Cognitive Load Analytics Platform.",
    version="1.0.0",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(health.router)
app.include_router(developer.router)
app.include_router(config.router)
app.include_router(analytics.router)
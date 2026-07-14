from fastapi import FastAPI
from backend.routes import health, developer

app = FastAPI(
    title="CogniStream API",
    description="Developer Flow-State & Cognitive Load Analytics",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(developer.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to CogniStream API"
    }
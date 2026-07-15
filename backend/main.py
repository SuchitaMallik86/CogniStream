from fastapi import FastAPI

from backend.routes import config, developer, health

app = FastAPI(
    title="CogniStream API",
    description="""
Developer Flow-State & Cognitive Load Analytics Platform.

CogniStream analyzes developer productivity by measuring flow state,
cognitive load, context switching, and coding patterns.

Developed as an internship project using FastAPI.
""",
    version="1.0.0",
    contact={
        "name": "CogniStream Team",
        "email": "support@cognistream.dev"
    },
    license_info={
        "name": "MIT License"
    }
)

app.include_router(health.router)
app.include_router(developer.router)
app.include_router(config.router)


@app.get("/", tags=["General"])
def home():
    return {
        "message": "Welcome to CogniStream API"
    }
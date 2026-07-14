from fastapi import FastAPI

app = FastAPI(
    title="CogniStream API",
    description="Developer Flow-State & Cognitive Load Analytics",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CogniStream API"
    }
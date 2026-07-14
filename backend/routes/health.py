from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "CogniStream",
        "version": "1.0.0"
    }
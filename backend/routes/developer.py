from fastapi import APIRouter

router = APIRouter()

@router.get("/developer")
def get_developer():
    return {
        "developer": "Demo Developer",
        "flow_state": "Focused",
        "coding_time": "120 minutes",
        "interruptions": 3
    }
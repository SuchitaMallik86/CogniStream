from fastapi import APIRouter

from backend.models.developer_model import DeveloperResponse
from backend.services.developer_service import get_developer_data

router = APIRouter(tags=["Developer"])


@router.get("/developer", response_model=DeveloperResponse)
def get_developer():
    return get_developer_data()
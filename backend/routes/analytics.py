from fastapi import APIRouter

from backend.models.analytics_model import AnalyticsResponse
from backend.services.analytics_service import calculate_productivity

router = APIRouter(tags=["Analytics"])


@router.get("/analytics", response_model=AnalyticsResponse)
def get_analytics():
    return calculate_productivity()
from fastapi import APIRouter

from backend.config.settings import (
    APP_NAME,
    APP_VERSION,
    ENVIRONMENT,
)

router = APIRouter(tags=["Configuration"])


@router.get("/config")
def get_configuration():
    return {
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
    }
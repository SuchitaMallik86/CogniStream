from pydantic import BaseModel


class DeveloperResponse(BaseModel):
    developer: str
    flow_state: str
    coding_time: str
    interruptions: int
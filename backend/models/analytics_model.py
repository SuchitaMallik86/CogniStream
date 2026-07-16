from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    flow_state: str
    context_switches: int
    productivity_score: int
    longest_flow_block: str
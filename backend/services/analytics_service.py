from backend.config.database import client
from backend.models.analytics_model import AnalyticsResponse


def calculate_productivity() -> AnalyticsResponse:
    total_events = client.query(
        "SELECT count() FROM cognistream.developer_events"
    ).result_rows[0][0]

    context_switches = client.query("""
        SELECT count()
        FROM cognistream.developer_events
        WHERE event_type NOT LIKE 'Coding%'
    """).result_rows[0][0]

    return AnalyticsResponse(
        flow_state="Focused",
        context_switches=context_switches,
        productivity_score=92,
        longest_flow_block=f"{total_events} events recorded"
    )
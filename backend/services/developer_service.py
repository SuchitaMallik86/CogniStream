from backend.models.developer_model import DeveloperResponse


def get_developer_data() -> DeveloperResponse:
    return DeveloperResponse(
        developer="Demo Developer",
        flow_state="Focused",
        coding_time="120 minutes",
        interruptions=3
    )
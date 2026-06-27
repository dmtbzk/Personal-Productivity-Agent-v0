from app.tools.statistics import get_statistics


def build_statistics_context() -> str:
    statistics = get_statistics()

    if not statistics:
        return "No productivity statistics found."

    return f"""
Productivity statistics:
{statistics}
"""
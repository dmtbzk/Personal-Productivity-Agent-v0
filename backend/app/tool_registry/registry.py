from app.tool_registry.todo_tools import TODO_TOOLS
from app.tool_registry.memory_tools import MEMORY_TOOLS
from app.tool_registry.statistics_tools import STATISTICS_TOOLS
from app.tool_registry.habit_tools import HABIT_TOOLS
from app.tool_registry.calendar_tools import CALENDAR_TOOLS


TOOLS = (
    TODO_TOOLS
    + MEMORY_TOOLS
    + STATISTICS_TOOLS
    + HABIT_TOOLS
    + CALENDAR_TOOLS
)


def get_allowed_tools(allowed_tool_names: list[str]):
    return [
        tool for tool in TOOLS
        if tool["name"] in allowed_tool_names
    ]
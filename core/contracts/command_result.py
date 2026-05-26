from typing import Any
from dataclasses import dataclass, field
from core.contracts.date_data import DateData
from core.contracts.flags_data import FlagsData
from core.contracts.error_data import ErrorData

@dataclass
class CommandResult:
    command: str
    action: str | None = None
    page_name: str | None = None
    task_id: str | None = None
    task_name: str | None = None
    date: DateData = field(
        default_factory=lambda: DateData(None, None, None, None)
    )
    flags: FlagsData = field(
        default_factory=lambda: FlagsData(None, None, None)
    )
    error: ErrorData = field(
        default_factory=lambda: ErrorData(False, None, None)
    )

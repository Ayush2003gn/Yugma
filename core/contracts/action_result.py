from typing import Any
from dataclasses import dataclass, field
from core.contracts.error_data import ErrorData

@dataclass
class ActionResult:
    success: bool = False,
    message: str | None = None,
    data: Any = None,
    error: ErrorData = field(
        default_factory=lambda: ErrorData(False, None, None)
    )
    
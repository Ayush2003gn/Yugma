from typing import Any
from dataclasses import dataclass, field
from core.contracts.error_data import ErrorData

@dataclass
class OperationResult:
    success: bool
    message: str | None = None
    data: Any = None
    error: ErrorData = field(
        default_factory=lambda: ErrorData(
            error_boolean= False,
            error_message = None,
            error_code = None
        )
    )
    
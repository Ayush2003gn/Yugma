from typing import Any
from dataclasses import dataclass, field
from core.contracts.error_data import ErrorData

@dataclass
class ValidationResult:
    value: Any = None
    is_valid: bool = False
    used_default: bool = False
    error: ErrorData = field(
        default_factory=lambda: ErrorData(False, None, None)
    )

@dataclass
class DateValidationResult:
    is_valid: bool
    day: int | None = None
    month: int | None = None
    year: int | None =  None
    week: int | None = None
    error: ErrorData = field(
        default_factory=lambda: ErrorData(False, None, None)
    )
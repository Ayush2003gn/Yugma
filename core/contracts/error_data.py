from typing import Any
from dataclasses import dataclass

@dataclass
class ErrorData:
    error_boolean: bool = False
    error_message: str | None = None
    error_code: str | None = None
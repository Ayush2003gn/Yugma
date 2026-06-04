from typing import Any
from dataclasses import dataclass

@dataclass
class FlagsData:
    priority: str | None = None
    status: bool | None = None
    default: bool | None = None


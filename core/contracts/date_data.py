from typing import Any
from dataclasses import dataclass

@dataclass
class DateData:
    day: int | None = None
    month: int | None = None
    year: int | None =  None
    week: int | None = None
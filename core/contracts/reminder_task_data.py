from typing import Any
from dataclasses import dataclass, field
import datetime
@dataclass
class ReminderTaskData:
    reminder_id: int
    task_iid: str
    task_page_id: str
    task_title: str
    reminder_time: datetime.datetime
    reminder_addition_message: str
    enabled: bool = field(default=True)
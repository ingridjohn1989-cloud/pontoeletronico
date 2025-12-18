from pydantic import BaseModel
from typing import Literal

class TimeEntryIn(BaseModel):
    user_id: str
    type: Literal[
        "checkIn",
        "lunchStart",
        "lunchEnd",
        "checkOut"
    ]

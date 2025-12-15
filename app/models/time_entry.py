from pydantic import BaseModel
from typing import Literal

class TimeEntryIn(BaseModel):
    type: Literal[
        "checkIn",
        "lunchStart",
        "lunchEnd",
        "checkOut"
    ]

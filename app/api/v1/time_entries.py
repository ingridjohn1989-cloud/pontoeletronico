from fastapi import APIRouter
from datetime import datetime

from app.models.time_entry import TimeEntryIn
from app.service import time_entry as service

router = APIRouter()


@router.post("")
def register_time_entry(payload: TimeEntryIn):
    entry = service.register_point(
        user_id="demo_user",
        entry_type=payload.type,
        timestamp=datetime.utcnow().isoformat()
    )

    return {
        "message": "Registro de ponto salvo com sucesso",
        "timeEntry": entry
    }


@router.get("/report")
def get_report(userId: str, month: int, year: int):
    entries = service.generate_report(userId, month, year)
    return {
        "userId": userId,
        "month": month,
        "year": year,
        "entries": entries
    }

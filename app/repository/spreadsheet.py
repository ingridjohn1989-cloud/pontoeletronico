import pandas as pd
from pathlib import Path
from uuid import uuid4

DATA_DIR = Path("app/storage")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_entry(user_id: str, entry_type: str, timestamp: str) -> dict:
    file = DATA_DIR / f"{user_id}.xlsx"

    row = {
        "id": str(uuid4()),
        "userId": user_id,
        "type": entry_type,
        "timestamp": timestamp
    }

    if file.exists():
        df = pd.read_excel(file)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_excel(file, index=False)
    return row


def load_entries(user_id: str) -> pd.DataFrame:
    file = DATA_DIR / f"{user_id}.xlsx"
    if not file.exists():
        return pd.DataFrame(columns=["id", "userId", "type", "timestamp"])
    return pd.read_excel(file)

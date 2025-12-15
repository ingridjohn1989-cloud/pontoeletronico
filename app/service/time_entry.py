import pandas as pd
from app.repository.spreadsheet import save_entry, load_entries


def register_point(user_id: str, entry_type: str, timestamp: str):
    return save_entry(user_id, entry_type, timestamp)


def generate_report(user_id: str, month: int, year: int):
    df = load_entries(user_id)

    if df.empty:
        return []

    df["dt"] = pd.to_datetime(df["timestamp"])
    df = df[
        (df["dt"].dt.month == month) &
        (df["dt"].dt.year == year)
    ]

    report = []

    for date, group in df.groupby(df["dt"].dt.date):
        report.append({
            "date": date.isoformat(),
            "entries": group[["type", "timestamp"]].to_dict(orient="records")
        })

    return report

import json
import sqlite3
from pathlib import Path

DB_PATH = Path("data/app.db")
OUT_PATH = Path("frontend/data.json")

def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS counter (
      date TEXT PRIMARY KEY,
      value INTEGER NOT NULL
    )
    """)

    rows = cur.execute("SELECT date, value FROM counter ORDER BY date ASC").fetchall()
    data = [{"date": d, "value": v} for (d, v) in rows]

    OUT_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    conn.close()

if __name__ == "__main__":
    main()


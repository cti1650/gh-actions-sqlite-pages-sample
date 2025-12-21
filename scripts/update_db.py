import sqlite3
from datetime import date
from pathlib import Path

DB_PATH = Path("data/app.db")

def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS counter (
      date TEXT PRIMARY KEY,
      value INTEGER NOT NULL
    )
    """)

    today = date.today().isoformat()

    # 前回までの最大値 + 1（初回は 1）
    next_value = cur.execute("SELECT COALESCE(MAX(value), 0) + 1 FROM counter").fetchone()[0]

    cur.execute(
        "INSERT OR REPLACE INTO counter (date, value) VALUES (?, ?)",
        (today, next_value),
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()


import sqlite3
from datetime import date
from pathlib import Path

DB_PATH = Path("data/app.db")
MAX_RECORDS = 2000

def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # テーブル作成
    cur.execute("""
    CREATE TABLE IF NOT EXISTS counter (
      date TEXT PRIMARY KEY,
      value INTEGER NOT NULL
    )
    """)

    today = date.today().isoformat()

    # 次の値（最大値 + 1）
    next_value = cur.execute(
        "SELECT COALESCE(MAX(value), 0) + 1 FROM counter"
    ).fetchone()[0]

    # 当日分 upsert
    cur.execute(
        "INSERT OR REPLACE INTO counter (date, value) VALUES (?, ?)",
        (today, next_value),
    )

    # ---- ここからレコード数制限 ----

    # レコード数を取得
    count = cur.execute("SELECT COUNT(*) FROM counter").fetchone()[0]

    if count > MAX_RECORDS:
        delete_count = count - MAX_RECORDS

        # 古い順に delete_count 件削除
        cur.execute(f"""
        DELETE FROM counter
        WHERE date IN (
          SELECT date FROM counter
          ORDER BY date ASC
          LIMIT {delete_count}
        )
        """)

    # ---- ここまで ----

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()

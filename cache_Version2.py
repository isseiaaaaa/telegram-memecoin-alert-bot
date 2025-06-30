import sqlite3
from typing import Optional

class SocialCache:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.execute("CREATE TABLE IF NOT EXISTS alerted (id TEXT PRIMARY KEY)")
        self.conn.commit()

    def is_alerted(self, token_id: str) -> bool:
        cur = self.conn.execute("SELECT 1 FROM alerted WHERE id=?", (token_id,))
        return bool(cur.fetchone())

    def mark_alerted(self, token_id: str):
        self.conn.execute("INSERT OR IGNORE INTO alerted (id) VALUES (?)", (token_id,))
        self.conn.commit()
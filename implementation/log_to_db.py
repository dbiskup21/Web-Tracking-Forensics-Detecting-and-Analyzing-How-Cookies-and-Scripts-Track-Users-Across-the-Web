import json
import sqlite3

DB_NAME = "tracking.db"
INPUT_FILE = "traffic_log_sanitized.json"

# 1. Spoj na bazu
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# 2. Kreiranje tablice
cursor.execute("""
CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    visited_site TEXT,
    request_domain TEXT,
    url TEXT,
    method TEXT,
    cookies TEXT,
    user_agent TEXT,
    is_third_party INTEGER
)
""")

# 3. Učitavanje JSON-a i unos u bazu
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        entry = json.loads(line)

        cursor.execute("""
        INSERT INTO requests (
            visited_site,
            request_domain,
            url,
            method,
            cookies,
            user_agent,
            is_third_party
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            entry.get("visited_site"),
            entry.get("request_domain"),
            entry.get("url"),
            entry.get("method"),
            ",".join(entry.get("cookies", [])),
            entry.get("user_agent"),
            int(entry.get("is_third_party", False))
        ))

conn.commit()
conn.close()

print("Podaci su uspješno spremljeni u tracking.db")
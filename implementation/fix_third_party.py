import sqlite3

conn = sqlite3.connect("tracking.db")
cur = conn.cursor()

cur.execute("""
UPDATE requests
SET is_third_party = 1
WHERE visited_site = ''
AND (
    request_domain LIKE '%microsoft.com%'
    OR request_domain LIKE '%facebook.com%'
    OR request_domain LIKE '%tiktok.com%'
)
""")

conn.commit()
conn.close()

print("Third-party oznake ispravljene za telemetry trackere.")
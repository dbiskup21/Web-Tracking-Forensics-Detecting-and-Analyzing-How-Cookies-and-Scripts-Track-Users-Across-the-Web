import sqlite3
import csv

conn = sqlite3.connect("tracking.db")
cur = conn.cursor()

cur.execute("""
SELECT visited_site, request_domain
FROM requests
WHERE is_third_party = 1
AND visited_site != ''
""")

rows = cur.fetchall()

with open("graph_edges.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["source", "target"])
    for site, domain in rows:
        writer.writerow([site, domain])

conn.close()

print("graph_edges.csv created")
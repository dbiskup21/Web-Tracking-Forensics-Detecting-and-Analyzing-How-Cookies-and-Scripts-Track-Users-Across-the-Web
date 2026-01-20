import sqlite3

conn = sqlite3.connect("tracking.db")
cur = conn.cursor()

print("=== OSNOVNE STATISTIKE ===")
cur.execute("SELECT COUNT(*) FROM requests")
print("Ukupan broj zapisa:", cur.fetchone()[0])

print("\n=== PRIMJER ZAPISA ===")
cur.execute("""
SELECT visited_site, request_domain, is_third_party, category
FROM requests
LIMIT 10
""")
for row in cur.fetchall():
    print(row)

print("\n=== TRACKERI PO KATEGORIJI ===")
cur.execute("""
SELECT category, COUNT(*)
FROM requests
WHERE is_third_party = 1
GROUP BY category
""")
for row in cur.fetchall():
    print(row)

conn.close()

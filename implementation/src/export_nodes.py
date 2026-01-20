import sqlite3
import csv

# Spoj na bazu
conn = sqlite3.connect("tracking.db")
cur = conn.cursor()

# Izvuci jedinstvene domene + kategoriju
# Ako domena ima vise kategorija, uzme se najcesca
cur.execute("""
SELECT request_domain,
       COALESCE(category, 'other') AS category,
       COUNT(*) as cnt
FROM requests
WHERE request_domain IS NOT NULL AND request_domain != ''
GROUP BY request_domain, category
ORDER BY request_domain, cnt DESC
""")

rows = cur.fetchall()

# Za svaku domenu zadrzi najcescu kategoriju
domain_category = {}
for domain, category, cnt in rows:
    if domain not in domain_category:
        domain_category[domain] = category

# Spremi u CSV
with open("graph_nodes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "category"])
    for domain, category in domain_category.items():
        writer.writerow([domain, category])

conn.close()

print("✔ graph_nodes.csv uspjesno generiran")

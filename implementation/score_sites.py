import sqlite3

DB_NAME = "tracking.db"

def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Kreiraj tablicu za rezultate (tracking intensity po stranici)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS site_scores (
        visited_site TEXT PRIMARY KEY,
        total_requests INTEGER,
        third_party_requests INTEGER,
        unique_third_party_domains INTEGER,
        advertising_requests INTEGER,
        analytics_requests INTEGER,
        social_requests INTEGER,
        telemetry_requests INTEGER,
        fp_like_requests INTEGER,
        tracking_intensity_score REAL
    )
    """)

    cur.execute("""
    SELECT
        visited_site,
        COUNT(*) AS total_requests,
        SUM(CASE WHEN is_third_party = 1 THEN 1 ELSE 0 END) AS third_party_requests,
        COUNT(DISTINCT CASE WHEN is_third_party = 1 THEN request_domain END) AS unique_third_party_domains,
        SUM(CASE WHEN category = 'advertising' THEN 1 ELSE 0 END) AS advertising_requests,
        SUM(CASE WHEN category = 'analytics' THEN 1 ELSE 0 END) AS analytics_requests,
        SUM(CASE WHEN category = 'social' THEN 1 ELSE 0 END) AS social_requests,
        SUM(CASE WHEN category = 'telemetry' THEN 1 ELSE 0 END) AS telemetry_requests,
        SUM(CASE WHEN fp_like = 1 THEN 1 ELSE 0 END) AS fp_like_requests
    FROM requests
    WHERE visited_site IS NOT NULL AND visited_site != ''
    GROUP BY visited_site
    """)

    rows = cur.fetchall()


    for r in rows:
        (site, total, tp, uniq_tp, adv, an, soc, tel, fp) = r

        score = (
            (tp or 0) * 1.0 +
            (uniq_tp or 0) * 5.0 +
            (adv or 0) * 2.0 +
            (an or 0) * 1.0 +
            (soc or 0) * 1.5 +
            (tel or 0) * 1.0 +
            (fp or 0) * 3.0
        )

        cur.execute("""
        INSERT INTO site_scores (
            visited_site,
            total_requests,
            third_party_requests,
            unique_third_party_domains,
            advertising_requests,
            analytics_requests,
            social_requests,
            telemetry_requests,
            fp_like_requests,
            tracking_intensity_score
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(visited_site) DO UPDATE SET
            total_requests=excluded.total_requests,
            third_party_requests=excluded.third_party_requests,
            unique_third_party_domains=excluded.unique_third_party_domains,
            advertising_requests=excluded.advertising_requests,
            analytics_requests=excluded.analytics_requests,
            social_requests=excluded.social_requests,
            telemetry_requests=excluded.telemetry_requests,
            fp_like_requests=excluded.fp_like_requests,
            tracking_intensity_score=excluded.tracking_intensity_score
        """, (site, total, tp, uniq_tp, adv, an, soc, tel, fp, score))

    conn.commit()


    cur.execute("""
    SELECT visited_site, tracking_intensity_score, third_party_requests, unique_third_party_domains
    FROM site_scores
    ORDER BY tracking_intensity_score DESC
    LIMIT 10
    """)
    top = cur.fetchall()

    print("=== TOP 10 web stranica po tracking_intensity_score ===")
    for row in top:
        print(row)

    conn.close()


if __name__ == "__main__":
    main()

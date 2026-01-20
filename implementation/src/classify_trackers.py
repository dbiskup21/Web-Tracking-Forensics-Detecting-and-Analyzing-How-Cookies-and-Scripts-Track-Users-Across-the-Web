import sqlite3

DB_NAME = "tracking.db"

# Pravila za kategorije (kao i prije)
TRACKER_RULES = {
    "analytics": [
        "google-analytics.com",
        "analytics.google.com",
        "googletagmanager.com",
        "ssl.gstatic.com",
    ],
    "advertising": [
        "doubleclick.net",
        "adsystem",
        "adservice",
        "criteo",
        "adnxs",
        "taboola",
        "outbrain",
    ],
    "telemetry": [
        "mobile.events.data.microsoft.com",
        "onecollector",
        "telemetry",
        "fp.msedge.net",
    ],
    "social": [
        "facebook.com",
        "fbcdn.net",
        "twitter.com",
        "tiktok.com",
        "linkedin.com",
        "instagram.com",
    ],
}

# Heuristike za "fingerprinting-like" (nije dokaz, nego indikator)
FP_URL_KEYWORDS = [
    "fingerprint",
    "fp=",
    "fp.",
    "canvas",
    "webgl",
    "beacon",
    "collect",
    "telemetry",
    "rum",
    "metrics",
]

def classify_domain(domain: str) -> str:
    domain = (domain or "").lower()
    for category, patterns in TRACKER_RULES.items():
        for p in patterns:
            if p in domain:
                return category
    return "other"


def is_fp_like(url: str, cookies_text: str, user_agent: str) -> int:
    """
    Vrlo jednostavna heuristika za sumnjive (fingerprinting-like) zahtjeve.
    1 = indikator, 0 = ne
    """
    url_l = (url or "").lower()
    cookies_l = (cookies_text or "").strip()
    ua_l = (user_agent or "").lower()

    # 1) Predugačak URL s puno parametara često je znak beacon/collect requesta
    if len(url_l) >= 220:
        return 1

    # 2) Ključne riječi u URL-u
    for kw in FP_URL_KEYWORDS:
        if kw in url_l:
            return 1

    # 3) Ako nema cookiesa, ali se šalje user-agent (često kod “cookie-less” praćenja)
    if cookies_l == "" and ("mozilla/" in ua_l):
        # Ovo je slab indikator, zato ga držimo kao "moguće"
        return 1

    return 0


def ensure_column(cur: sqlite3.Cursor, table: str, col: str, coltype: str) -> None:
    """
    Dodaj stupac ako ne postoji (SQLite nema IF NOT EXISTS za ALTER u svim slučajevima).
    """
    cur.execute(f"PRAGMA table_info({table})")
    cols = [r[1] for r in cur.fetchall()]
    if col not in cols:
        cur.execute(f"ALTER TABLE {table} ADD COLUMN {col} {coltype}")


def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Osiguraj da postoje stupci category i fp_like
    ensure_column(cur, "requests", "category", "TEXT")
    ensure_column(cur, "requests", "fp_like", "INTEGER")

    # Dohvati samo third-party zahtjeve (na njima ima smisla raditi klasifikaciju)
    cur.execute("""
        SELECT id, request_domain, url, cookies, user_agent
        FROM requests
        WHERE is_third_party = 1
    """)
    rows = cur.fetchall()

    for row_id, domain, url, cookies_text, user_agent in rows:
        category = classify_domain(domain)
        fp_flag = is_fp_like(url, cookies_text, user_agent)

        cur.execute(
            "UPDATE requests SET category = ?, fp_like = ? WHERE id = ?",
            (category, fp_flag, row_id)
        )

    conn.commit()
    conn.close()
    print("Klasifikacija trackera završena (+ fp_like indikator dodan).")


if __name__ == "__main__":
    main()

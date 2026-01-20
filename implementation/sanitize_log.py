import json

INPUT_FILE = "traffic_log.json"
OUTPUT_FILE = "traffic_log_sanitized.json"

def sanitize_entry(entry):
    sanitized = {
        "visited_site": entry.get("visited_site", ""),
        "request_domain": entry.get("request_domain", ""),
        "url": entry.get("url", "").split("?")[0],  # uklanja query string
        "method": entry.get("method", ""),
        "cookies": list(entry.get("cookies", {}).keys()),
        "user_agent": entry.get("user_agent", "")
    }

    sanitized["is_third_party"] = (
        sanitized["visited_site"] != "" and
        sanitized["visited_site"] != sanitized["request_domain"]
    )

    return sanitized


with open(INPUT_FILE, "r", encoding="utf-8") as infile, \
     open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:

    for line in infile:
        entry = json.loads(line)
        clean = sanitize_entry(entry)
        outfile.write(json.dumps(clean) + "\n")

print("Sanitized log created:", OUTPUT_FILE)
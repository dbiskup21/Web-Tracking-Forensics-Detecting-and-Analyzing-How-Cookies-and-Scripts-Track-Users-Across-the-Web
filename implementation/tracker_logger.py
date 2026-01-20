from mitmproxy import http
import json

def request(flow: http.HTTPFlow):
    referer = flow.request.headers.get("referer", "")
    site = referer.split("/")[2] if "://" in referer else ""

    entry = {
        "visited_site": site,
        "request_domain": flow.request.host,
        "url": flow.request.pretty_url,
        "method": flow.request.method,
        "cookies": dict(flow.request.cookies),
        "user_agent": flow.request.headers.get("user-agent", "")
    }

    with open("traffic_log.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
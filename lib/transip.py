import niquests

def patch(domain: str, record: str, ip: str, token: str) -> None:
    headers = get_headers(token)
    payload = get_payload(ip, record)
    url = f"https://api.transip.nl/v6/domains/{domain}/dns"

    with niquests.patch(url, json=payload, headers=headers) as req:
        req.raise_for_status()

def get_payload(ip: str, record: str) -> dict:
    return {
        "dnsEntry": {
            "name": record,
            "content": ip,
            "expire": 300,
            "type": "A"
        }
    }

def get_headers(token: str) -> dict:
    return {
        "Authorization":f"Bearer {token}"
    }
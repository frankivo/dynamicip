from . import crypto

import niquests

class transip:
    def __init__(self, key: str) -> None:
        self.key = key
        self.sign(key, "test")

    def patch(self, domain: str, record: str, ip: str, token: str) -> None:
        headers = self.get_headers(token)
        payload = self.get_payload(ip, record)
        url = f"https://api.transip.nl/v6/domains/{domain}/dns"

        with niquests.patch(url, json=payload, headers=headers) as req:
            req.raise_for_status()

    def get_payload(self, ip: str, record: str) -> dict:
        return {
            "dnsEntry": {
                "name": record,
                "content": ip,
                "expire": 300,
                "type": "A"
            }
        }

    def get_headers(self, token: str) -> dict:
        return {
            "Authorization":f"Bearer {token}"
        }

    def auth():
        pass

    def sign(self, key: str, data: str) -> str:
        crypto.sign(key, data)

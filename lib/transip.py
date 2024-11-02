from . import util
from datetime import datetime, timedelta

import json
import niquests
import uuid

class transip:
    def __init__(self, private_key: str, domain: str, record: str, login: str) -> None:
        self.domain = domain
        self.record = record
        self.token = transip.token_handler(private_key, login)

    class token_handler:
        def __init__(self, key: str, login: str) -> None:
            self.key = key
            self.login = login

            self.token_bearer = None
            self.token_expire = datetime.now()

        def get(self) -> str:
            if self.__is_expired():
                self.__auth()
            return self.token_bearer

        def __auth(self):
            payload = self.__get_payload()
            signature = util.sign_with_private_key(self.key, json.dumps(payload))
            headers = { "Signature": signature }

            with niquests.post("https://api.transip.nl/v6/auth", json=payload, headers=headers) as req:
                req.raise_for_status()
                self.token_bearer = req.json()["token"]
                self.token_expire = datetime.now() + timedelta(hours=1)

        def __get_payload(self) -> dict:
            return {
                "login": self.login,
                "nonce": self.__nonce(),
                "read_only": False,
                "expiration_time": "1 hour",
                "label": f"dyndns {datetime.now()}",
                "global_key": True
            }

        def __nonce(self) -> str:
            return str(uuid.uuid4()).replace("-", "")

        def __is_expired(self) -> bool:
            return datetime.now() > self.token_expire

    def patch(self, ip: str) -> None:
        headers = self.__get_headers()
        payload = self.__get_payload(ip)
        url = f"https://api.transip.nl/v6/domains/{self.domain}/dns"

        with niquests.patch(url, json=payload, headers=headers) as req:
            req.raise_for_status()
            print(f"ip updated: {ip}")

    def __get_payload(self, ip: str) -> dict:
        type = "A" if "." in ip else "AAAA"

        return {
            "dnsEntry": {
                "name": self.record,
                "content": ip,
                "expire": 300,
                "type": type
            }
        }

    def __get_headers(self) -> dict:
        return {
            "Authorization":f"Bearer {self.token.get()}"
        }

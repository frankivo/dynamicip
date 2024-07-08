from . import crypto
from datetime import datetime

import niquests

class transip:
    def __init__(self, private_key: str, domain: str, record: str) -> None:
        self.token = transip.token_handler(private_key, domain, record)

    class token_handler:
        def __init__(self, key: str, domain: str, record: str) -> None:
            self.domain = domain
            self.record = record
            self.key = key

            self.token_bearer = None
            self.token_expire = datetime.now()

        def get(self) -> str:
            if self.__is_expired():
                self.__auth()
            return self.token_bearer
        
        def __auth(self):
            pass

        def __is_expired(self) -> bool:
            return datetime.now() > self.token_expire

    def patch(self, ip: str) -> None:
        headers = self.__get_headers()
        payload = self.__get_payload(ip)
        url = f"https://api.transip.nl/v6/domains/{self.domain}/dns"

        with niquests.patch(url, json=payload, headers=headers) as req:
            req.raise_for_status()

    def __get_payload(self, ip: str) -> dict:
        return {
            "dnsEntry": {
                "name": self.record,
                "content": ip,
                "expire": 300,
                "type": "A"
            }
        }

    def __get_headers(self) -> dict:
        return {
            "Authorization":f"Bearer {self.token.get()}"
        }
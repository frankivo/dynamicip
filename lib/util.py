import base64

import niquests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


def try_load_dotenv():
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

def get_wan_ip4():
    with niquests.get("https://api.ipify.org?format=json") as req:
        req.raise_for_status()
        res = req.json()
        return res["ip"]

def get_wan_ip6():
    with niquests.get("https://api6.ipify.org?format=json") as req:
        req.raise_for_status()
        res = req.json()
        return res["ip"]

def sign_with_private_key(key: str, data: str) -> str:
    pkey = serialization.load_pem_private_key(
        key.replace("\\n", "\n").encode(), password=None
    )
    signature = pkey.sign(
        data.encode(),
        padding.PKCS1v15(),
        hashes.SHA512(),
    )
    return base64.b64encode(signature).decode("utf-8")

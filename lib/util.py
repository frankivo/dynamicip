from OpenSSL import crypto
import base64
import niquests
import OpenSSL

def try_load_dotenv():
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass

def get_wan_ip():
    with niquests.get("https://api.ipify.org?format=json") as req:
        req.raise_for_status()
        res = req.json()
        return res["ip"]

def sign_with_private_key(key: str, data: str) -> str:
    pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key.replace("\\n", "\n"))
    sign = OpenSSL.crypto.sign(pkey, data, "sha512") 
    bytes = base64.b64encode(sign)
    return bytes.decode('utf-8') 

from OpenSSL import crypto
import OpenSSL
import base64

def sign(key: str, data: str) -> str:
    pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key.replace("\\n", "\n"))
    sign = OpenSSL.crypto.sign(pkey, data, "sha512") 
    return base64.b64encode(sign)

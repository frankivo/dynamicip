import niquests

def get_ip():
    with niquests.get("https://api.ipify.org?format=json") as req:
        req.raise_for_status()
        res = req.json()
        return res["ip"]

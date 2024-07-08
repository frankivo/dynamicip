from lib import ip, util
from lib.transip import transip

import os
import time

def main():
    DOMAIN = os.environ["DOMAIN"]
    DOMAIN_RECORD = os.environ["DOMAIN_RECORD"]
    SLEEP_TIME_SECONDS = int(os.getenv("SLEEP_TIME_SECONDS", "3600")) # Default: 1 hour
    KEY = os.environ["KEY"]

    dns = transip(private_key=KEY, domain=DOMAIN, record=DOMAIN_RECORD)

    my_ip = "0.0.0.0"

    while True:
        time.sleep(SLEEP_TIME_SECONDS)

        current_ip = ip.get_ip()
        if not current_ip == my_ip:
            print(f"new ip: {current_ip}")
            my_ip = current_ip
            dns.patch(my_ip)


if __name__ == '__main__':
    util.try_load_dotenv()
    main()
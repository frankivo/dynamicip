from lib import ip, util
from lib.transip import transip

import os
import time

def main():
    SLEEP_TIME_SECONDS = int(os.getenv("SLEEP_TIME_SECONDS", "3600")) # Default: 1 hour
    dns = transip(
        private_key = os.environ["KEY"],
        domain = os.environ["DOMAIN"],
        record = os.environ["DOMAIN_RECORD"],
        login = os.environ["LOGIN"]
    )

    my_ip = "0.0.0.0"

    while True:
        current_ip = ip.get_ip()
        if not current_ip == my_ip:
            print(f"new ip: {current_ip}")
            my_ip = current_ip
            dns.patch(my_ip)

        time.sleep(SLEEP_TIME_SECONDS)


if __name__ == '__main__':
    util.try_load_dotenv()
    main()
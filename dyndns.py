from lib import util
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
    my_ipv4, my_ipv6 = ("127.0.0.1", "::1")

    while True:
        current_ip4 = util.get_wan_ip4()
        current_ip6 = util.get_wan_ip6()

        if not (current_ip4 == my_ipv4 or current_ip6 == my_ipv6):
            my_ipv4 = current_ip4
            my_ipv6 = current_ip6

            dns.patch(my_ipv4)
            dns.patch(my_ipv6)

        time.sleep(SLEEP_TIME_SECONDS)


if __name__ == '__main__':
    util.try_load_dotenv()
    main()

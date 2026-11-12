import os
import time

from lib import util
from lib.transip import transip


def main():
    SLEEP_TIME_SECONDS = int(os.getenv("SLEEP_TIME_SECONDS", "3600")) # Default: 1 hour
    dns = transip(
        private_key = os.environ["KEY"],
        domain = os.environ["DOMAIN"],
        record = os.environ["DOMAIN_RECORD"],
        login = os.environ["LOGIN"],
    )
    ipv6_enabled = os.getenv("ENABLE_IPV6", "true").lower() == "true"

    my_ipv4, my_ipv6 = ("127.0.0.1", "::1")

    while True:
        current_ip4 = util.get_wan_ip4()
        if (current_ip4 != my_ipv4):
            my_ipv4 = current_ip4
            dns.patch(my_ipv4)

        if ipv6_enabled:
            current_ip6 = util.get_wan_ip6()
            if current_ip6 != my_ipv6:
                my_ipv6 = current_ip6
                dns.patch(my_ipv6)

        time.sleep(SLEEP_TIME_SECONDS)


if __name__ == "__main__":
    util.try_load_dotenv()
    main()

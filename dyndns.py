from lib import ip, util

import os
import time

def main():
    SLEEP_TIME_SECONDS = int(os.getenv("SLEEP_TIME_SECONDS", "3600")) # Default: 1 hour

    my_ip = "0.0.0.0"

    while True:
        time.sleep(SLEEP_TIME_SECONDS)

        current_ip = ip.get_ip()
        if not current_ip == my_ip:
            my_ip = current_ip

if __name__ == '__main__':
    util.try_load_dotenv()
    main()
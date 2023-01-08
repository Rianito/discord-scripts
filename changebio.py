# alterar o bio do discord de tempo em tempo

import os
import requests
import time

authorization = os.getenv("authorization")
bios = [
    ""
]

while True:
    for bio in bios:
        try:
            requests.patch("https://discord.com/api/v9/users/@me",
                           json={"bio": bio}, headers={"authorization": authorization})
        except:
            pass
        time.sleep(10)

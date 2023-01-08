# ficar ligando pro mocorongo

import os
import requests
import time

authorization = os.getenv("authorization")
channel_id = 0
recipients = [
    0,
]

while True:
    try:
        requests.post(f"https://discord.com/api/v9/channels/{channel_id}/call/ring", json={
            "recipients": recipients}, headers={"authorization": authorization})
    except:
        pass
    time.sleep(1)

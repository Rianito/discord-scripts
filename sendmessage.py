# floodar chat

import os
import requests
import time

authorization = os.getenv("authorization")
channel_id = 0
message = ""

while True:
    try:
        requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", json={
                      "content": message}, headers={'authorization': authorization})
    except:
        pass
    time.sleep(1)

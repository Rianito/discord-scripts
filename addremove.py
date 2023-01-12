# adicionar e remover da conversa

import os
import requests
import time

authorization = os.getenv("authorization")

channel_id = 0
user_id = 0

while True:
    try:
        requests.put(f"https://discord.com/api/v9/channels/{channel_id}/recipients/{user_id}", headers={
                     "authorization": authorization})
        time.sleep(1)
        requests.delete(
            f"https://discord.com/api/v9/channels/{channel_id}/recipients/{user_id}", headers={"authorization": authorization})
    except:
        pass
    time.sleep(1)

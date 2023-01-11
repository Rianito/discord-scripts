import requests
import os
import time

authorization = os.getenv("authorization")
whitelist = [
    "0",
]

friends = requests.get("https://discord.com/api/v9/users/@me/relationships",
                       headers={"authorization": authorization}).json()

for friend in friends:
    friend_id = friend["id"]
    if friend["id"] not in whitelist:
        while True:
            try:
                response = requests.delete(
                    f"https://discord.com/api/v9/users/@me/relationships/{friend_id}", headers={"authorization": authorization})
                if response.status_code == 204:
                    break
            except:
                pass
            time.sleep(1)

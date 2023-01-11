# deleta as mensagens de um usuário em um canal

import os
import requests
import time

authorization = os.getenv("authorization")
channel_id = 933379881042051102
user_id = 901087361541242880
messages = requests.get(
    f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100", headers={"authorization": authorization}).json()

for message in messages:
    if message["author"]["id"] == str(user_id):
        while True:
            try:
                response = requests.delete(
                    f"https://discord.com/api/v9/channels/{channel_id}/messages/{message['id']}", headers={"authorization": authorization})
                if response.status_code == 204:
                    break
            except:
                pass
            time.sleep(1)

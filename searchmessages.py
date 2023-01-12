# procura todas as mensagens de um usuário em um servidor

import os
import requests
import time


authorization = os.getenv("authorization")
guild_id = 0
author_id = 0


def searchMessages(guild_id, author_id, offset):
    response = requests.get(
        f"https://discord.com/api/v9/guilds/{guild_id}/messages/search?author_id={author_id}&offset={offset}", headers={"authorization": authorization})
    content = response.json()
    if response.status_code == 200:
        for message in content["messages"]:
            print(
                f"{message[0]['author']['username']}: {message[0]['content']}")
        if content["total_results"] >= offset + 25:
            searchMessages(guild_id, author_id, offset + 25)
        else:
            print("Acabou.")
    else:
        print(f"{response.status_code}: {content['message']}")
        time.sleep(content["retry_after"])
        searchMessages(guild_id, author_id, offset)

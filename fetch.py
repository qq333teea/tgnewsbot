import os
from telethon import TelegramClient, events, sync

api_creds = open(".api", "r").readlines()

api_id = int(api_creds[0])
print(int(api_creds[0]))
api_hash = api_creds[1]

client = TelegramClient('session_name', api_id, api_hash)
client.start()
 

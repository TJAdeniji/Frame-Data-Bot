import discord 
import logging
import requests 

import os 
from dotenv import load_dotenv 

from bs4 import BeautifulSoup

load_dotenv()

token = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode='w')

client = discord.Client(intents=intents)

#moves have IDs to be used  
@client.event
async def on_message(message):
        if message.author == client.user:
                return
        if message.content.startswith("$hello"):
                embed = discord.Embed(title = "Sample Embed", url = "https://dreamcancel.com/wiki/The_King_of_Fighters_XV/Kula_Diamond")
                await message.channel.send(embed = embed)

client.run(token, log_handler = handler)
import discord
import logging
# import requests
# import bs4 from BeautifulSoup

intents = discord.Intents.default()
intents.message_content = True
handler - logging .FileHandler(filename="discord.log", encoding="utf-8", mode='w')
token = "MTA3MjU3NDU1ODY4ODc4ODUwMA.GNlHoV.sfXSHzWGrubedaWSAeHjdm0GMHchJzolqpZWF0"

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
        if message.author == client.user:
                return
        if message.content.startswith("$hello"):
                embed = discord.Embed(title = "Sample Embed", url = "https://dreamcancel.com/wiki/The_King_of_Fighters_XV/Kula_Diamond">
                await message.channel.send(embed = embed)
#    print(message.author.name + " said, " + message.content)
#    if not message.author.id == "1072574558688788500":
#            await client.send_message(message.channel, content = "GOT EM! TIME TO STYLE ON EM WITH A CLIMAX"

client.run(token, logging_handler = handler)
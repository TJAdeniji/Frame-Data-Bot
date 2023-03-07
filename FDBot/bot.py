import discord 
from discord.ext import commands

import logging
import requests 
from bs4 import BeautifulSoup 

import os 
from dotenv import load_dotenv 


load_dotenv()

token = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode='w')

bot = commands.Bot(command_prefix="?", intents=intents)

#
# 

#3/1 - command Method to get the char's name, then the move or special in another method?
# all moves follow a name_move convention in the table, might be an easy way to locate them when scraping. 

#3/3 text-align: center is the location for all the rows with the data for the move list
#might hard code the labels, at least for now for simplicity's sake.

# @bot.command()
# async def char(ctx, *, arg):

#         await ctx.send(arg)



#
#Bot not syncing commands to server.  
#


@bot.event
async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('------')

# @bot.command(name="sync", description="Owner only")
# async def sync(interaction: discord.Interaction):
#         if interaction.user.id == 213820249420595200:
#                 await bot.tree.sync()
#                 print('Command tree synced.')
#         else:
#                 await interaction.response.send_message('You must be the owner to use this command!')

@bot.event
async def on_message(message):
        if message.user.id == 213820249420595200 and message.content.startsWith("$sync"):
                bot.tree.sync()
                await bot.process_commands(message)
                print('Command tree synced.')
        else:
                await message.response.send_message('You must be the owner to use this command!')
         
@bot.tree.command(name="char", description="select a character")
async def char(interaction: discord.Interaction):
        pass
        
@bot.event
async def on_message(message):
        if message.author == bot.user:
                return
        
        if message.content.startswith("$hello"):
                URL = "https://dreamcancel.com/wiki/The_King_of_Fighters_XV/"
                r = requests.get(URL)
                soup = BeautifulSoup(r.content, 'html5lib')
                #moveList = r.find_all("div", class_ = "float:right")
                #r = requests.get(URL + charName + "/Data"
                embed = discord.Embed(title = "Sample Embed", url = "https://dreamcancel.com/wiki/The_King_of_Fighters_XV/")
                embed.set_thumbnail(url = "")
                embed.add_field(name="Damage", value="Damage", inline="True")
                embed.add_field(name="Guard", value="Guard", inline="True")
                embed.add_field(name="Cancel", value="Cancel", inline="True")
                embed.add_field(name="Startup", value="Startup", inline="True")
                embed.add_field(name="Recovery", value="Recovery", inline="True")
                embed.add_field(name="Hit Advantage", value="Hit Advantage", inline="True")
                embed.add_field(name="Block Advantage", value="Block Advantage", inline="True")
                embed.add_field(name="Invulnerability", value="Invulnerability", inline="True")
                embed.add_field(name="Stun", value="Stun", inline="True")
                embed.add_field(name="Guard Damage", value="Guard Damage", inline="True")
                await message.channel.send(embed = embed)

bot.run(token, log_handler = handler)
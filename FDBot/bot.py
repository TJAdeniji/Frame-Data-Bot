import discord 
from discord import app_commands
from discord.ext import commands
from typing import Literal, Optional
from discord.ext.commands import Greedy, Context

import logging
import requests 
from bs4 import BeautifulSoup 

import os 
from dotenv import load_dotenv 

import aiohttp
import asyncio

load_dotenv()

token = os.getenv("TOKEN")
intents = discord.Intents.all()
intents.message_content = True
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode='w')

bot = commands.Bot(command_prefix="!", intents=intents)

selected_char = ""
page_char = ""

roster = {
     "shunei": "Shun'ei",
     "meitenkun": "Meitenkun", 
     "benimaru": "Benimaru_Nikaido",
     "ash": "Ash_Crimson",
     "elisabeth": "Elisabeth_Blanctorche",
     "kukri": "Kukri",
     "kyo": "Kyo_Kusanagi",
     "iori": "Iori_Yagami",
     "chizuru": "Chizuru_Kagura",
     "k": "K'",
     "maxima": "Maxima",
     "whip": "Whip",
     "isla": "Isla",
     "heidern": "Heidern",
     "dolores": "Dolores",
     "terry": "Terry_Bogard",
     "andy": "Andy_Bogard",
     "joe": "Joe_Higashi",
     "ryo": "Ryo_Sakazaki",
     "robert": "Robert_Garcia",
     "king": "King",
     "yashiro": "Yashiro_Nanakase",
     "shermie": "Shermie",
     "chris": "Chris",
     "athena": "Athena_Asamiya",
     "mai": "Mai_Shiranui",
     "yuri": "Yuri_Sakazaki",
     "leona": "Leona_Heidern",
     "ralf": "Ralf_Jones",
     "clark": "Clark_Still",
     "antonov": "Antonov",
     "ramon": "Ramón",
     "kod": "King_of_Dinosaurs",
     "krohnen": "Krohnen",
     "kula": "Kula_Diamond",
     "angel": "Ángel",
     "bluemary": "Blue_Mary",
     "vanessa": "Vanessa",
     "luong": "Luong",
     "rock": "Rock_Howard",
     "bjenet": "B.Jenet",
     "gato": "Gato",
     "geese": "Geese_Howard",
     "billy": "Billy_Kane",
     "yamazaki": "Ryuji_Yamazaki",
     "oyashiro": "Orochi_Yashiro",
     "oshermie": "Orochi_Shermie",
     "ochris": "Orochi_Chris",
     "haohmaru": "Haohmaru",
     "nakoruru": "Nakoruru",
     "darli": "Darli_Dagger",
     "orugal": "Omega_Rugal",
     "shingo": "Shingo_Yabuki",    
     "kim": "Kim_Kaphwan"
}


@bot.event
async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('------')              
             
@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(
  ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.") 

@bot.tree.command(name="char", description="select a character")
async def char(interaction: discord.Interaction, selected_char: str):
        
        if selected_char in roster:
            page_char = roster.get(selected_char)
        else:
            page_char = selected_char
            
        URL = (f"https://dreamcancel.com/wiki/The_King_of_Fighters_XV/{page_char}/Data")
        async with aiohttp.ClientSession() as session:
             async with session.get(URL) as resp:
                  print(resp.status)
                  data = await resp.text()
        soup = BeautifulSoup(data, 'html5lib')
        print(soup.prettify())
        raw_moveList = soup.find_all("table", "wikitable")
        
        
        #moveList = r.find_all("div", class_ = "float:right")
        #r = requests.get(URL + charName + "/Data"
        charEmbed = discord.Embed(title = "Sample Embed", url = URL)
        charEmbed.set_thumbnail(url = "")
        charEmbed.add_field(name="Damage", value="Damage", inline="True")
        charEmbed.add_field(name="Guard", value="Guard", inline="True")
        charEmbed.add_field(name="Cancel", value="Cancel", inline="True")
        charEmbed.add_field(name="Startup", value="Startup", inline="True")
        charEmbed.add_field(name="Recovery", value="Recovery", inline="True")
        charEmbed.add_field(name="Hit Advantage", value="Hit Advantage", inline="True")
        charEmbed.add_field(name="Block Advantage", value="Block Advantage", inline="True")
        charEmbed.add_field(name="Invulnerability", value="Invulnerability", inline="True")
        charEmbed.add_field(name="Stun", value="Stun", inline="True")
        charEmbed.add_field(name="Guard Damage", value="Guard Damage", inline="True")
        await interaction.response.defer()
        await interaction.followup.send(embed = charEmbed)


bot.run(token, log_handler = handler)
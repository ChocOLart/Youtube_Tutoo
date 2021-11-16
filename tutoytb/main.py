# Importation du module discord

import asyncio
from random import randint
import discord

from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(intents=intents, command_prefix=",")


@bot.event
async def on_ready():
    print("Bot prét")
    await bot.change_presence(activity=discord.Game(name="Rich Presence Here"))



@bot.event
async def on_ready():
    print('Bot Prét')




jeton = "BOT_TOKEN"

bot.run(jeton)

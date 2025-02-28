from python_aternos import Client
from dotenv import load_dotenv
from os import getenv
import discord
from discord.ext import commands

# Load environment variables from .env file
atclient = Client()
load_dotenv("./src/.env")

# Log in - Aternos
atclient.login(getenv("USERNAME"), getenv("PASSWORD"))
aternos = atclient.account
servers = aternos.list_servers()

# Log in - Discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Commands - Discord
@bot.command()
async def status(ctx):
  await ctx.send(servers[0].status)

@bot.command()
async def start(ctx):
  servers[0].start()
  await ctx.send("Server started...\nPlease wait for a few minutes.")

# Start the bot
bot.run(getenv("DISCORD_TOKEN"))
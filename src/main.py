from dotenv import load_dotenv
from os import getenv
from aternos import Aternos
import discord
from discord.ext import commands

# Load environment variables from .env file
load_dotenv("./src/.env")
aternosServer = Aternos(getenv('ATERNOS_USERNAME'), getenv('ATERNOS_PASSWORD'))


# Log in - Discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def list_servers(ctx):
    servers = aternosServer.servers
    if not servers:
        await ctx.send("No servers found.")
        return

    server_list = "\n".join([f"{i+1}. {server.address} | {server.status}" for i, server in enumerate(servers)])
    await ctx.send(f"Available servers:\n{server_list}")

# Commands - Discord
@bot.command()
async def status(ctx, server_number: int):
    server = aternosServer.get_server(int(server_number))
    if server:
        await ctx.send(f"Status of {server.address}: {server.status}")
    else:
        await ctx.send(f"Server '{server_number}' not found.")

@bot.command()
async def start(ctx, server_number: int):
    aternosServer.start_server(int(server_number))
    await ctx.send("Server started...\nPlease wait for a few minutes.")

# Start the bot
bot.run(getenv("DISCORD_TOKEN"))
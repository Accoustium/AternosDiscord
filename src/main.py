from dotenv import load_dotenv
from aternos import Aternos
from discord import DiscordBot
from os import getenv


# Load environment variables from .env file
load_dotenv("./src/.env")
aternosServer = Aternos(getenv('ATERNOS_USERNAME'), getenv('ATERNOS_PASSWORD'))

# Log in - Discord
discord = DiscordBot(command_prefix='!', aternosServer=aternosServer)
discord.run(getenv('DISCORD_TOKEN'))
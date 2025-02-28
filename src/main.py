from python_aternos import Client
from dotenv import load_dotenv
from os import getenv

atclient = Client()
load_dotenv("./src/.env")

# Log in
atclient.login(getenv("USERNAME"), getenv("PASSWORD"))
aternos = atclient.account

servers = aternos.list_servers()

print(servers[0].status)

class DiscordBot(discord.Client):
  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True
client = DiscordBot(intents=intents)
client.run(getenv("DISCORD_TOKEN"))
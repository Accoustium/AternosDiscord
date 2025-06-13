import dotenv
from .aternos_bot import Aternos
from .discord_bot import DiscordBot
import os
from string import Template


# Global variables
PATH = os.path.dirname(os.path.abspath(__file__))

# Build .env file
# This file should contain your Aternos and Discord credentials
ENV_TEMPLATE = Template("""
ATERNOS_USERNAME = "$aternos_username"
ATERNOS_PASSWORD = "$aternos_password"
DISCORD_TOKEN = "$discord_token"
DISCORD_GUILD_ID = "$discord_guild_id"
DISCORD_CHANNEL_ID = "$discord_channel_id"
""")


class EnvBuilder:
    def __init__(self):
        self.build_env_file()

    def build_env_file(self):
        # Accept credential from user input
        vars = []
        for _ in ["Aternos Username", "Aternos Password", "Discord Token", "Discord Guild ID", "Discord Channel ID"]:
            var = input(f"Enter your Aternos and Discord credentials ({ _ }): ")
            vars.append(var)

        # Create .env file with the provided credentials
        env_content = ENV_TEMPLATE.substitute(
            aternos_username=vars[0],
            aternos_password=vars[1],
            discord_token=vars[2],
            discord_guild_id=vars[3],
            discord_channel_id=vars[4]
        )
        with open(os.path.join(PATH, '.env'), 'w') as env_file:
            env_file.write(env_content)



class AternosDiscordBot:
    def __init__(self, aternos_username, aternos_password, discord_token, discord_guild_id, discord_channel_id):
        # Load environment variables
        self.aternos_server = Aternos(os.getenv('ATERNOS_USERNAME'), os.getenv('ATERNOS_PASSWORD'))
        self.discord_bot = DiscordBot(command_prefix='!', aternosServer=self.aternos_server)

    def run(self):
        # Set up Discord bot
        self.discord_bot.run(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    # Load environment variables from .env file
    dotenv.load_dotenv(os.path.join(PATH, '.env'))

    if not all(os.getenv(var) for var in ['ATERNOS_USERNAME', 'ATERNOS_PASSWORD', 'DISCORD_TOKEN', 'DISCORD_GUILD_ID', 'DISCORD_CHANNEL_ID']):
        # If any environment variable is missing, prompt user to create .env file
        print("Missing environment variables. Please create a .env file with your credentials.")
        EnvBuilder()
        dotenv.load_dotenv(os.path.join(PATH, '.env'))

    # Initialize the bot with credentials from environment variables
    bot = AternosDiscordBot(
        aternos_username=os.getenv('ATERNOS_USERNAME'),
        aternos_password=os.getenv('ATERNOS_PASSWORD'),
        discord_token=os.getenv('DISCORD_TOKEN'),
        discord_guild_id=os.getenv('DISCORD_GUILD_ID'),
        discord_channel_id=os.getenv('DISCORD_CHANNEL_ID')
    )

    # Run the bot
    bot.run()

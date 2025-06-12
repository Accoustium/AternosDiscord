import discord
from discord.ext import commands


class DiscordBot(commands.Bot):
    def __init__(self, command_prefix='!', intents=None, aternosServer=None):
        if intents is None:
            intents = discord.Intents.default()
            intents.message_content = True
        super().__init__(command_prefix=command_prefix, intents=intents)

        self.server = aternosServer

    async def list_servers(self, ctx):
        servers = self.server.servers
        if not servers:
            await ctx.send("No servers found.")
            return

        server_list = "\n".join([f"{i + 1}. {server.address} | {server.status}" for i, server in enumerate(servers)])
        await ctx.send(f"Available servers:\n{server_list}")


    async def status(self, ctx, server_number: int):
        server = self.server.get_server(int(server_number))
        if server:
            await ctx.send(f"Status of {server.address}: {server.status}")
        else:
            await ctx.send(f"Server '{server_number}' not found.")


    async def start(self, ctx, server_number: int):
        self.server.start_server(int(server_number))
        await ctx.send("Server started...\nPlease wait for a few minutes.")

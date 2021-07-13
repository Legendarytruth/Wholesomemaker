import os
import random
import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option


class ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="ping", description="Check the Bot Latency.")
    async def ping(self, ctx: SlashContext):
        embed = discord.Embed(
            description=f"🏓 Pong! **{round(self.client.latency * 1000)} ms**")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ping(client))

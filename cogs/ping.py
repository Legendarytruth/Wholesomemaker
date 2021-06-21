import os
import random
import discord
from discord.ext import commands


class ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
                    description=f"🏓 Pong! **{round(self.client.latency * 1000)} ms**")
        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(ping(client))

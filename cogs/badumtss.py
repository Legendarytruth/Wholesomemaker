import os
import random
import discord
from discord.ext import commands


class badumtss(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def badumtss(self, ctx):
        await ctx.message.delete()
        await ctx.send(f'https://media.tenor.com/images/d67d16cb84b78151763312767bb4e555/tenor.gif')


def setup(client):
    client.add_cog(badumtss(client))

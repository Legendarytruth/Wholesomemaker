import os
import random
import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option


class badumtss(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="badumtss", description="Cosplaying yourself as Yan👍")
    @commands.has_role(845586428057354253)
    async def badumtss(self, ctx: SlashContext):
        await ctx.send(f'https://media.tenor.com/images/d67d16cb84b78151763312767bb4e555/tenor.gif')


def setup(client):
    client.add_cog(badumtss(client))

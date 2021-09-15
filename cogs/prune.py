import os
import random
import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
import asyncio


class prune(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="prune",
                       description="Clear Messages from a Channel.",
                       options=[
                           create_option(
                               name="amount",
                               description="How many message want to be yeeted out?",
                               option_type=4,
                               required=True
                           )
                       ])
    @commands.has_role(825578057498099732)
    async def prune(self, ctx: SlashContext, amount):
        await ctx.channel.purge(limit=amount)
        # Gets the message the bots just sent.
        embed = discord.Embed(
            description=f"<:check:839158727512293406> Pruned {amount} Messages!")
        botsMessage = await ctx.send(embed=embed)
        # Waits for 3 seconds before continuing to the next line of code
        await asyncio.sleep(3)
        await botsMessage.delete()

    @prune.error
    async def prune_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&825578057498099732> roles to use this command!")
            await ctx.send(embed=embed, hidden=True)


def setup(client):
    client.add_cog(prune(client))

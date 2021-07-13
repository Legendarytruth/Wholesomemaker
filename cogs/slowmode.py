import os
import random
import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option


class slowmode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="slowmode",
                       description="Slow down the chats.",
                       options=[
                           create_option(
                               name="seconds",
                               description="Provide the time.",
                               option_type=4,
                               required=True
                           )
                       ])
    @commands.has_role(825578057498099732)
    async def slowmode(self, ctx: SlashContext, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        embed = discord.Embed(
            description=f"<:check:839158727512293406> Slowmode has been enabled for this channel.")
        await ctx.send(embed=embed)

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&825578057498099732> roles to use this command!")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(slowmode(client))

import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
from discord import Embed
from typing import Optional
import datetime
import asyncio


class unmute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="unmute",
                       description="Unmute a user.",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person Should I Unmute?",
                               option_type=6,
                               required=True
                           )
                       ])
    @commands.has_role(825578057498099732)
    async def unmute(self, ctx: SlashContext, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(role)
        embed = discord.Embed(
            description=f"<:check:839158727512293406> Successfully unmuted {member.mention}.")
        await ctx.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&825578057498099732> roles to use this command!")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(unmute(client))

import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
from discord import Embed
from typing import Optional
import datetime
import asyncio


class ghostorg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="ghostorg",
                       description="Assign/Detach Ghost Organization Roles to a User.",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person Should I Assign/Detach Ghost Org.?",
                               option_type=6,
                               required=True
                           )
                       ])
    @commands.has_role(825578057498099732)
    async def ghostorg(self, ctx: SlashContext, *, member: discord.Member):

        role = discord.utils.get(ctx.guild.roles, name='ghost org.')
        if role in member.roles:
            await member.remove_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{member.mention}** Has Been removed from <@&840846226630377492> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)
        else:
            await member.add_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{member.mention}** Has Been Given <@&840846226630377492> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)

    @ghostorg.error
    async def ghostorg_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&825578057498099732> roles to use this command!")
            await ctx.channel.send(embed=embed, hidden=True)


def setup(client):
    client.add_cog(ghostorg(client))

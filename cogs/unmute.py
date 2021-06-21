import discord
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio


class unmute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        if member is None:
            await ctx.send('Please pass in a valid user by mentioning them or using their ID.')
            return
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(role)
        embed = discord.Embed(
            description=f"<:check:839158727512293406> Successfully unmuted {member.mention}.")
        await ctx.channel.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description=f"'<:cross:839158779815657512> You must have the `Kick Members` permission to use this command!")
            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(unmute(client))

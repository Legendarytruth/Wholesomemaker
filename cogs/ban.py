import discord
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio


class ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user_id, *, reason: Optional[str] = "No reason provided."):
        user = await self.client.fetch_user(user_id)
        await ctx.message.delete()
        try:
            await user.send(f'You have been banned from **{ctx.guild}** for the following reason: {reason}')
        except:
            embed = discord.Embed(
                    description=f"<:cross:839158779815657512> Failed to send DM to <@{user_id}>. They probably had their DM's closed.")
            await ctx.channel.send(embed=embed)
        await ctx.guild.ban(user, reason=reason)
        embed = discord.Embed(
                    description=f"<:check:839158727512293406> Successfully banned {user} for: {reason}")
        await ctx.channel.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                    description=f"<:cross:839158779815657512> You must have the `Ban Members` permission to use this command!")
            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(ban(client))

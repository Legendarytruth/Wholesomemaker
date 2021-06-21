import os
import random
import discord
from discord.ext import commands


class unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        embed = discord.Embed(
                    description=f"<:check:839158727512293406> Successfully unbanned {user.mention}")
        await ctx.channel.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                    description=f"<:cross:839158779815657512> You must have the `Ban Members` permission to use this command!")
            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(unban(client))

import os
import random
import discord
from discord.ext import commands


class slowmode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['slow'])
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.message.delete()
        embed = discord.Embed(
                    description=f"<:check:839158727512293406> Slowmode has been enabled for this channel.")
        await ctx.channel.send(embed=embed)

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            embed = discord.Embed(
                    description=f"<:cross:839158779815657512> You must have the `Manage Channels` permission to use this command!")
            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(slowmode(client))

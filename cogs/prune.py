import os
import random
import discord
from discord.ext import commands


class prune(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['clear', 'delete', 'purge'])
    @commands.has_permissions(manage_messages=True)
    async def prune(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)

    @prune.error
    async def prune_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Manage Messages` permission to use this command!")
            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(prune(client))

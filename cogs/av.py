import os
import random
import discord
from discord.ext import commands


class av(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['avatar'])
    async def av(self, ctx, *, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(
            title=f"{member.name}'s Avatar", color=discord.Color.blue())
        embed.set_image(url=member.avatar_url)
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(av(client))

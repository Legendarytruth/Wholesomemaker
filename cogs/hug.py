import discord
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp


class hug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hug(self, ctx, *, member: discord.Member = None):

        if member is None:
            member = ctx.author

        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get('https://some-random-api.ml/animu/hug')
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = discord.Embed(
            title=f"**{ctx.author.name}** hugging **{member.name}** <a:rooLove:839188637773594674>", color=discord.Color.purple())  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson['link'])
        embed.set_footer(
            text=f"Powered by some-random-api.ml API😉")
        await ctx.send(embed=embed)  # Send the embed


def setup(client):
    client.add_cog(hug(client))

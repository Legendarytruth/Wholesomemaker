import discord
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp


class meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get('https://some-random-api.ml/meme')
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = discord.Embed(
            title=dogjson['caption'], color=discord.Color.purple())  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson['image'])
        embed.set_footer(
            text=f"Category : {dogjson['category']} | Powered by some-random-api.ml API😉")
        await ctx.send(embed=embed)  # Send the embed


def setup(client):
    client.add_cog(meme(client))

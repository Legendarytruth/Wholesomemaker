import discord
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp


class smug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def smug(self, ctx):
        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get('https://neko-love.xyz/api/v1/smug')
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = discord.Embed(
            title=f"**{ctx.author.name}**, Here's some Smug pics <a:SmugGirl:841526768699179008>", color=discord.Color.purple())  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson['url'])
        embed.set_footer(
            text=f"Powered by neko-love.xyz API😉")
        await ctx.send(embed=embed)  # Send the embed


def setup(client):
    client.add_cog(smug(client))

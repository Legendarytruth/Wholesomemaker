import discord
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp


class dog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()  # Convert it to a JSON dictionary
        # This time we'll get the fact request as well!
            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request2.json()
        embed = discord.Embed(
            title="Doggo! <a:rooCute:839162904414257162>", color=discord.Color.purple())  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.add_field(name="Did you know?",
                        value=f"{factjson['fact']}", inline=False)
        embed.set_image(url=dogjson['link'])
        embed.set_footer(
            text=f"Powered by some-random-api.ml API😉")
        await ctx.send(embed=embed)  # Send the embed


def setup(client):
    client.add_cog(dog(client))

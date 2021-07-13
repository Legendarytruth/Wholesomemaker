import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp
from discord_slash import *
from discord_slash.utils.manage_commands import create_option


class dog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="dog", description="Provide you with some Dog Pics and Facts.")
    async def dog(self, ctx: SlashContext):
        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get('https://dog.ceo/api/breeds/image/random')
            dogjson = await request.json()  # Convert it to a JSON dictionary
        # This time we'll get the fact request as well!
            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request2.json()
        embed = discord.Embed(
            title=":dog: Doggo!", color=discord.Color.purple())  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.add_field(name="Did you know?",
                        value=f"{factjson['fact']}", inline=False)
        embed.set_image(url=dogjson['message'])
        embed.set_footer(
            text=f"Powered by some-random-api.ml and dog.ceo API😉")
        await ctx.send(embed=embed)  # Send the embed


def setup(client):
    client.add_cog(dog(client))

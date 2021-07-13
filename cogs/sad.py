import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp


class sad(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="sad", description="😭😭")
    async def sad(self, ctx: SlashContext):
        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get('https://neko-love.xyz/api/v1/cry')
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = discord.Embed(
            title=f"**{ctx.author.name}** is sad <:sadge:841528068651876413>", color=discord.Color.purple())  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson['url'])
        embed.set_footer(
            text=f"Powered by neko-love.xyz API😉")
        await ctx.send(embed=embed)  # Send the embed


def setup(client):
    client.add_cog(sad(client))

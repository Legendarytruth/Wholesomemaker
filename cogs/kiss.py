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


class kiss(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="kiss",
                       description="Kiss someone OwO",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person?",
                               option_type=6,
                               required=True
                           )])
    async def kiss(self, ctx: SlashContext, *, member: discord.Member):

        if member == ctx.author:
            return await ctx.send(":neutral_face: W.. wait, You can't kiss yourself.. \n How ruud you are :pensive:")

        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get('https://neko-love.xyz/api/v1/kiss')
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = discord.Embed(
            title=f"**{ctx.author.display_name}** kissing **{member.display_name}** :kissing_heart:", color=discord.Color.purple())  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson['url'])
        embed.set_footer(
            text=f"Powered by neko-love.xyz API😉")
        await ctx.send(embed=embed)  # Send the embed


def setup(client):
    client.add_cog(kiss(client))

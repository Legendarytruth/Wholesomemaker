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


class hug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="hug",
                       description="Give Hug to a User",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person?",
                               option_type=6,
                               required=False
                           )])
    async def hug(self, ctx, *, member: discord.Member = None):

        if member == ctx.author:
            return await ctx.send(":neutral_face: W.. wait, You can't hug yourself.. \n How ruud you are :pensive:")

        if member is None:
            return await ctx.send(":neutral_face: W.. wait, You can't hug yourself.. \n How ruud you are :pensive:")

        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get('https://some-random-api.ml/animu/hug')
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = discord.Embed(
            title=f"**{ctx.author.display_name}** hugging **{member.display_name}** <a:rooLove:839188637773594674>", color=discord.Color.purple())  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson['link'])
        embed.set_footer(
            text=f"Powered by some-random-api.ml API😉")
        await ctx.send(embed=embed)  # Send the embed


def setup(client):
    client.add_cog(hug(client))

import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp
from discord_slash import *
from discord.ext.commands import cooldown, BucketType
from discord_slash.utils.manage_commands import create_option


class konesyntees(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="konesyntees",
                       description="Use superior Estonian technology to express your feelings like you've never before!",
                       options=[
                           create_option(
                               name="input",
                               description="Konesyntezing input",
                               option_type=3,
                               required=True
                           ), create_option(
                               name="voice",
                               description="Choose the voice the synthesizer will uses (optional)",
                               option_type=4,
                               required=False
                           ), create_option(
                               name="speed",
                               description="Configure how the voice the synthesizer will goes (optional)",
                               option_type=4,
                               required=False
                           )
                       ])
    async def konesyntees(self, ctx: SlashContext, input: str, voice: Optional[int] = 1, speed: Optional[int] = -4):

        if len(str(input)) > 100:
            return await ctx.reply("Text too long! (<100)", hidden=True)

        if len(str(input)) < 5:
            return await ctx.reply("An error occurred: the command must have some sort of params", hidden=True)

        if input is None:
            return await ctx.reply("the text can't be empty", hidden=True)

        if voice > 3:
            return await ctx.reply("voice must be in the range of 0 .. 3", hidden=True)

        if speed < -9:
            return await ctx.reply("speed must be in the range of -9 .. 9", hidden=True)

        if speed > 9:
            return await ctx.reply("speed must be in the range of -9 .. 9", hidden=True)

        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get(f"https://teenus.eki.ee/konesyntees?haal={voice}&kiirus={speed}&tekst={input}")
            konesynteesjson = await request.json()  # Convert it to a JSON dictionary
            # Send the embed
            return await ctx.send(f"{konesynteesjson['mp3url']}")


def setup(client):
    client.add_cog(konesyntees(client))

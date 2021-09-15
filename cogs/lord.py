import os
from dotenv import load_dotenv
import random
import discord
from discord import Embed
from pymongo import MongoClient
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle

load_dotenv()

cluster = MongoClient(os.getenv("MONGODB_URL"))

ucer = cluster["discord"]["taco"]


class lord(commands.Cog):
    def __init__(self, client):
        self.client = client

    @ cog_ext.cog_slash(name="lord", description="Shows you the name of the richest of em' all!")
    @ commands.cooldown(1, 5, commands.BucketType.user)
    async def lord(self, ctx: SlashContext):
        rankings = ucer.find().sort("xp", -1)
        mescount = ucer.find().sort("messagecount", -1)
        i = 1
        embed = discord.Embed(
            title=f"Statistics", colour=discord.Colour.blurple())
        for x in rankings:
            try:
                temp = await ctx.guild.fetch_member(x["id"])
                tempxp = x["xp"]
                tacocount = x["taco_count"]
                embed.add_field(
                    name=f"_ _", value=f"{i}. **<{temp.display_name}>** - Taco : {tacocount} | XP : {tempxp}", inline=False)
                i += 1
            except:
                pass
            if i == 11:
                break
        return await ctx.send(embed=embed)

    def better_time(self, cd: int):
        time = f"{cd} seconds"
        if cd > 60:
            minutes = cd - (cd % 60)
            seconds = cd - minutes
            minutes = int(minutes / 60)
            time = f"{minutes} minutes {seconds} seconds"
        if minutes > 60:
            hoursglad = minutes - (minutes % 60)
            hours = int(hoursglad / 60)
            minutes = minutes - (hours*60)
            time = f"{hours} hours {minutes} minutes"
        return time

    @lord.error  # command name error
    async def lord_error(self, ctx, error):  # define error
        # tells the bot its a cool down error
        if isinstance(error, commands.CommandOnCooldown):
            # msg is the message you would like to send, the format is how it formats the seconds left.
            cd = round(error.retry_after)
            if cd == 0:
                cd = 1
            # msg is the message you would like to send, the format is how it formats the seconds left.
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.display_name}** you need to wait {self.better_time(cd)} to use that command again.", colour=discord.Colour.red())
        await ctx.send(embed=embed)  # sends the error message to the channel


def setup(client):
    client.add_cog(lord(client))

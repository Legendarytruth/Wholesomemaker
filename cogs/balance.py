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


class balance(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="balance", description="Shows you how many tacos you have.")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def balance(self, ctx: SlashContext):

        member = ctx.author
        lemao = ctx.author.display_name

        stats = ucer.find_one({"id": member.id})

        if stats is None:
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> **{member.display_name}** You don't have any tacos!", colour=discord.Colour.red())
            await ctx.send(embed=embed)
        else:
            tacocount = stats["taco_count"]
            xpcount = stats["xp"]
            await ctx.send(f"**{lemao}** You have {tacocount} tacos :taco:")

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

    @balance.error  # command name error
    async def balance_error(self, ctx, error):  # define error
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
    client.add_cog(balance(client))

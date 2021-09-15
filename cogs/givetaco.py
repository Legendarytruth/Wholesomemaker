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


class givetaco(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="givetaco",
                       description="Allows you to transfer taco to another user.",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person?",
                               option_type=6,
                               required=True
                           ),
                           create_option(
                               name="amount",
                               description="How much taco did you want give?",
                               option_type=4,
                               required=True
                           )
                       ])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def givetaco(self, ctx: SlashContext, member: discord.Member, amount: int):
        sender = ucer.find_one({"id": ctx.author.id})
        receiver = ucer.find_one({"id": member.id})

        pengirim = sender["taco_count"]
        penerima = receiver["taco_count"]
        xp = sender["xp"]
        xp1 = receiver["xp"]
        msgauthor = sender["messagecount"]
        msguser = receiver["messagecount"]
        imgauthor = sender["image_url"]
        imguser = receiver["image_url"]

        if member == ctx.author:
            return await ctx.send("You can't give taco to yourself.")

        if pengirim < 0:
            return await ctx.send("You don't have enough taco to give.")

        if pengirim > 0:
            pengirim -= amount
            penerima += amount

            ucer.update_one({"id": ctx.author.id}, {
                "$set": {"taco_count": pengirim, "xp": xp, "username": ctx.author.name, "discrim": ctx.author.discriminator, "messagecount": msgauthor, "image_url": imgauthor}})

            ucer.update_one({"id": member.id}, {
                "$set": {"taco_count": penerima, "xp": xp1, "username": member.name, "discrim": member.discriminator, "messagecount": msguser, "image_url": imguser}})

            return await ctx.send(f"Successfully transferred taco's!")

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

    @givetaco.error  # command name error
    async def givetaco_error(self, ctx, error):  # define error
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
    client.add_cog(givetaco(client))

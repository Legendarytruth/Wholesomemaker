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


class eat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="eat", description="Eat a single taco in front of everyone.")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def eat(self, ctx: SlashContext):

        gifs = ["https://media3.giphy.com/media/3oKIPay5G3yCBXo3le/giphy.gif",
                "https://media4.giphy.com/media/TJrhuGPiZlUeXhJ4jI/giphy.gif",
                "https://media1.giphy.com/media/82okobf2F12rNV3XqD/giphy.gif",
                "https://media2.giphy.com/media/26BRDpgF3iwXFkEQU/giphy.gif",
                "https://media0.giphy.com/media/3CgHKSDwAT92o/giphy.gif",
                "https://media2.giphy.com/media/13VJu6tRPDBF72/giphy.gif",
                "https://media3.giphy.com/media/fBDHF3FYQ4ygaXw1HW/giphy.gif"]

        quotes = ["Grrrrr.", "One does not simply eat more than one taco at a time.", "<takes taco>", "Watch over your tacos, as one just got swallowed!", "Thank you for choosing TACO Airlines, enjoy your flight", "Don't get taconstipated!", "Now listen to the Taco Song!", "If you eat too much, you'll become T H I C C",
                  "For Kingdom and Glory!", "All hail the Taco bot!", "If you don’t like tacos, I’m nacho type.", "Taco big or taco home", "I ate a taco and all I got was this lousy message", "Taco to you later", "One step farther from the taco throne.", "OM NOM NOM", "AAAH IT BURNS TOO SPICY!!"]

        member = ctx.author
        lemao = ctx.author.display_name

        stats = ucer.find_one({"id": member.id})
        total_taco = stats["taco_count"]

        if total_taco == 0:
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> **{member.display_name}** You don't have any tacos!", colour=discord.Colour.red())
            return await ctx.send(embed=embed)
        else:
            osas = stats["xp"]
            osis = stats["messagecount"]
            nambah_taco = stats["taco_count"] - 1
            img = str(ctx.author.avatar_url)
            ucer.update_one({"id": ctx.author.id}, {
                "$set": {"taco_count": nambah_taco, "xp": osas, "username": ctx.author.name, "discrim": ctx.author.discriminator, "messagecount": osis, "image_url": img}})

            embed = discord.Embed(title=f"{ctx.author.display_name} just ate a delicious taco! :taco:",
                                  description=f"{random.choice(quotes)}", colour=discord.Colour.green())
            embed.set_image(url=random.choice(gifs))
            embed.set_footer(text=f"Image Source: Giphy.com")
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

    @eat.error  # command name error
    async def eat_error(self, ctx, error):  # define error
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
    client.add_cog(eat(client))

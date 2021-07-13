import discord
import discord_slash.cog_ext
from discord.ext import commands
from pymongo import MongoClient
from discord.ext.commands import cooldown, BucketType
from discord_slash import *
from discord_slash.utils.manage_commands import create_option

bot_channel = 808958457855344640  # restrict rep check on #bot-commands channel

cluster = MongoClient(
    "your mongodb uri")

reps = cluster["discord"]["rep"]


class rep(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        wholesome = "<:Wholesome:825035249532403802>"
        if payload.emoji == wholesome:
            stats = reps.find_one({"id": payload.user_id})
            if stats is None:
                newuser = ({"id": payload.user_id, "reactcount": 1})
                reps.insert_one(newuser)
            else:
                kung = stats["reactcount"] + 1
                reps.update_one(
                    {"id": payload.user_id, "reactcount": kung})

    @cog_ext.cog_slash(name="rep",
                       description="Know how many Wholesome react you give to someone message.",
                       options=[
                           create_option(
                               name="member",
                               description="Sees this User Rep.",
                               option_type=6,
                               required=False
                           )
                       ])
    async def rep(self, ctx: SlashContext, *, member:  discord.Member = None):

        if member is None:
            member = ctx.author

        if ctx.channel.id == bot_channel:
            stats = reps.find_one({"id": member.id})

            if stats is None:
                await ctx.send(f"Your <:Wholesome:825035249532403802> count: 0")
            else:
                await ctx.send(f"Your <:Wholesome:825035249532403802> count: ")
        else:
            return await ctx.send(f"<:cross:839158779815657512> **{member.name}**, that command is disabled in this channel.")


def setup(client):
    client.add_cog(rep(client))

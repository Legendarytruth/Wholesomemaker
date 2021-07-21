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
        if str(payload.emoji) == wholesome:
            stats = reps.find_one({"id": payload.user_id})
            if stats is None:
                newuser = ({"id": payload.user_id, "reactcount": 1})
                reps.insert_one(newuser)
            else:
                kung = stats["reactcount"] + 1
                reps.update_one({"id": payload.user_id}, {
                    "$set": {"reactcount": kung}})

    @cog_ext.cog_slash(name="rep", description="Know how many Wholesome react you give to someone message.")
    async def rep(self, ctx: SlashContext):
        stats = reps.find_one({"id": ctx.author.id})
        kung = stats["reactcount"]

        if ctx.channel.id == bot_channel:

            if stats is None:
                await ctx.send(f"Your <:Wholesome:825035249532403802> count: 0")
            else:
                await ctx.send(f"Your <:Wholesome:825035249532403802> count: {kung}")
        else:
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.display_name}**, that command is disabled in this channel.")
            return await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="toprep", description="Rankings for most Wholesome emojis sent.")
    async def toprep(self, ctx: SlashContext):
        if (ctx.channel.id == bot_channel):
            rankings = reps.find().sort("reactcount", -1)
            i = 1
            embed = discord.Embed(
                title=f"Statistics", colour=discord.Colour.blurple())
            for x in rankings:
                try:
                    temp = await ctx.guild.fetch_member(x["id"])
                    tempxp = x["reactcount"]
                    embed.add_field(name=f"_ _",
                                    value=f"{i}. **<{temp.display_name}>** - <:Wholesome:825035249532403802> x {tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
            await ctx.send(embed=embed)
        else:
            return await ctx.send(f"<:cross:839158779815657512> **{ctx.member.name}**, that command is disabled in this channel.")


def setup(client):
    client.add_cog(rep(client))

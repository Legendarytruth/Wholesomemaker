import os
import random
import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
from typing import Optional
from pymongo import MongoClient
from discord.ext.commands import cooldown, BucketType

# talk_channels is the most used channel (which in this case is all channels in Wholesome Series Videos)

talk_channels = [818815530647158784, 818815613266952193, 808958457855344640, 837680350716362814, 815213963871911996, 828968512146898954, 839444297542533140, 825272629559951390,
                 826078465781661736, 826078419888242708, 837720268918882305, 837665514654138480, 829866889937289257, 824809146641154130, 834312211454754826, 834312245571747842,
                 817712543795249182, 816763959931043861]

cluster = MongoClient(
    "your mongodb uri")

kicked = cluster["discord"]["kicks"]


class kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    # this cog.listener is to log all people kick count, based on sending a message. there is no problem at all.. move along folks :)
    @commands.Cog.listener()
    async def on_message(self, message):
        kicks = kicked.find_one({"id": message.author.id})
        if message.channel.id in talk_channels:
            if not message.author.bot:
                if kicked is None:
                    newuser = {"id": message.author.id,
                               "kickcount": 0, "reason": 0}
                    kicked.insert_one(newuser)

    @cog_ext.cog_slash(name="kick",
                       description="Kick a user.",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person Should I Kick?",
                               option_type=6,
                               required=True
                           ),
                           create_option(
                               name="reason",
                               description="Provide the Reason (Optional)",
                               option_type=3,
                               required=False
                           )
                       ])
    @commands.has_role(845586428057354253)  # dispatch role (head moderators)
    async def kick(self, ctx: SlashContext, member:  discord.Member, *, reason: Optional[str] = "No reason provided."):
        kicks = kicked.find_one({"id": ctx.member.id})
        if kicks is None:
            newuser = {"id": member.id,
                       "kickcount": 1, "reason": 0}
            kicked.insert_one(newuser)
            await member.send(f'You have been kicked on **{ctx.guild}** for the following reason: {reason}')
            embed = discord.Embed(
                description=f"<:check:839158727512293406> Successfully Kicked {member} for: {reason}")
            await ctx.send(embed=embed)
            await member.kick(reason=reason)
            channel = self.client.get_channel(
                831215570631393392)  # server-logs channel
            embed = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** kicks **{member.mention}** for following reason : {reason}", colour=discord.Colour.green())
            await channel.send(embed=embed)
        else:
            kickcounts = kicked["kickcount"] + 1
            kicked.update_one({"id": member.id}, {"$set": {
                "kickcount": kickcounts, "reason": reason}})
            await member.send(f'You have been kicked on **{ctx.guild}** for the following reason: {reason}')
            embed = discord.Embed(
                description=f"<:check:839158727512293406> Successfully Kicked {member} for: {reason}")
            await ctx.send(embed=embed)
            await member.kick(reason=reason)
            channel = self.client.get_channel(
                831215570631393392)  # server-logs channel
            embed = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** kicks **{member.mention}** for following reason : {reason}", colour=discord.Colour.green())
            await channel.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&845586428057354253> roles to use this command!")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(kick(client))

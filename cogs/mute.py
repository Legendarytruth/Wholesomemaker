import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
from discord import Embed
from typing import Optional
import datetime
import os
from dotenv import load_dotenv
import asyncio
from pymongo import MongoClient
from discord.ext.commands import cooldown, BucketType

load_dotenv()

cluster = MongoClient(os.getenv("MONGODB_URL"))

muted = cluster["discord"]["muted"]


class mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="mute",
                       description="Mute a user.",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person Should I Mute?",
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
    @commands.has_role(825578057498099732)
    async def mute(self, ctx: SlashContext, member: discord.Member, *, reason: str):

        stats = muted.find_one({"id": member.id})
        if stats is None:
            role = discord.utils.get(
                ctx.guild.roles, name='suffering from dunning kruger')
            await member.add_roles(role, reason=reason)
            muted.insert_one(
                {"id": member.id, "mutecount": 1, "reason": reason})
            channel = self.client.get_channel(831215570631393392)
            embed = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** mute **{member.mention}** for following reason : {reason}", colour=discord.Colour.green())
            await channel.send(embed=embed)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{member.mention}** has been muted for following reason : {reason}", colour=discord.Colour.green())
            await ctx.send(embed=success)
            return await member.send(f'You have been muted on **{ctx.guild}** for the following reason: {reason}')
        else:
            role = discord.utils.get(
                ctx.guild.roles, name='suffering from dunning kruger')
            await member.add_roles(role, reason=reason)
            mutecount = stats["mutecount"] + 1
            muted.update_one({"id": member.id}, {"$set": {
                "mutecount": mutecount, "reason": reason}})
            channel = self.client.get_channel(831215570631393392)
            embed = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** mute **{member.mention}** for following reason : {reason}", colour=discord.Colour.green())
            await channel.send(embed=embed)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{member.mention}** has been muted for following reason : {reason}", colour=discord.Colour.green())
            await ctx.send(embed=success)
            await member.send(f'You have been muted on **{ctx.guild}** for the following reason: {reason}')

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&825578057498099732> roles to use this command!")
            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(mute(client))

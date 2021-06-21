import discord
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
from pymongo import MongoClient
from discord.ext.commands import cooldown, BucketType

cluster = MongoClient(
    "your mongodb databases")

muted = cluster["discord"]["muted"]


class mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member = None, *, reason: str):

        if member is None:
            ctx.send(
                f"<:cross:839158779815657512> {ctx.author.mention} You can't mute yourself.")

        stats = muted.find_one({"id": member.id})
        if stats is None:
            role = discord.utils.get(ctx.guild.roles, name='Muted')
            await member.add_roles("Muted", reason=reason)
            muted.insert_one(
                {"id": member.id, "mutecount": 1, "reason": reason})
            channel = self.client.get_channel(831215570631393392)
            embed = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** mute **{member.mention}** for following reason : {reason}", colour=discord.Colour.green())
            await channel.send(embed=embed)
            return await member.send(f'You have been muted on **{ctx.guild}** for the following reason: {reason}')
        else:
            role = discord.utils.get(ctx.guild.roles, name='Muted')
            await member.add_roles(role, reason=reason)
            mutecount = stats["mutecount"] + 1
            muted.update_one({"id": member.id}, {"$set": {
                "mutecount": mutecount, "reason": reason}})
            channel = self.client.get_channel(831215570631393392)
            embed = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** mute **{member.mention}** for following reason : {reason}", colour=discord.Colour.green())
            await channel.send(embed=embed)
            await member.send(f'You have been muted on **{ctx.guild}** for the following reason: {reason}')

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Kick Members` permission to use this command!")
            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(mute(client))

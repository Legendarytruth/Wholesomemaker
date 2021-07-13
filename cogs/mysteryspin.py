import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp
import random

bot_channel = 808958457855344640


class mysteryspin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="mysteryspin",
                       description="Spin the Mystery Wheel and Get More Booming Prize!",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person?",
                               option_type=6,
                               required=False
                           )
                       ])
    @commands.has_role(825578057498099732)
    async def mysteryspin(self, ctx: SlashContext, *, member: discord.Member = None):

        if member is None:
            member = ctx.author

        ans = [f"{member.mention} spinned the Mystery Spin and got 10 P’s & Q’s Snacks. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got 10 Meteorite Snacks. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got 10 EgoChaser Snacks. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got 5 Pißwasser Drinks. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got 5 eCola Drinks. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got Pack of Redwood. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got 10 P’s & Q’s Snacks. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and hit the Jackpot and got 50,000XP <:FennPOG:839189820668248135>. \n XP will be awarded within 24h. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got Full Ammo \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got $25,000. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got 5 eCola Drinks. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got 25.000 Chips. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got A Random Special Cargo Item. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got Mystery Vehicle (a.k.a. Limited Access to Private Lounge for a Day). \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got All Snacks Replenished. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and got Resupplied Bunker. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and hit the Fucking Jackpot and got 100,000XP <:FennPOG:839189820668248135>. \n XP will be awarded within 24h. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and hit the Fucking Fuck Jackpot and got 150,000XP <:FennPOG:839189820668248135>. \n XP will be awarded within 24h. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and hit the Fucking Fucker Fuck Jackpot and got 200,000XP <:FennPOG:839189820668248135>. \n XP will be awarded within 24h. \n You can spin the wheel again in 24h.",
               f"{member.mention} spinned the Mystery Spin and hit the Pogn't Jackpot and got XP Reset <:FennPOG:839189820668248135>. \n XP will be resetted within 24h. \n You can spin the wheel again in 24h.",
               ]

        if ctx.channel.id == bot_channel:
            #embed = discord.Embed(colour=discord.Colour.green())
            # embed = discord.Embed(
            #    description=f'{random.choice(ans)}', colour=discord.Colour.green())
            # embed.set_footer(
            #    text=f"Congratulations, Winners of Mystery Wheel!", icon_url="https://cdn.discordapp.com/emojis/816783243109335100.png?v=1")
            await ctx.send(f"{random.choice(ans)}")
        else:
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.name}**, that command is disabled in this channel.")
            await ctx.channel.send(embed=embed)

    @mysteryspin.error
    async def mysteryspin_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&825578057498099732> roles to use this command!")
            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(mysteryspin(client))

import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp
import random
from discord.ext.commands import cooldown, BucketType
from discord_slash import *
from discord_slash.utils.manage_commands import create_option

bot_channel = 808958457855344640


class wheelspin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="wheelspin", description="Spin the wheel and Get some Prize!")
    @commands.cooldown(1, 10800, commands.BucketType.user)
    async def wheelspin(self, ctx: SlashContext):
        ans = [f"{ctx.author.mention} spinned the Lucky Wheel and got Sent to Kamurocho. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Muted for 10 Minutes <:GTASeriesVideos:839162693415206962>. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Sent to Sotenbori. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Free Round Trip to Cayo Perico. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 10 P’s & Q’s Snacks. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 10 Meteorite Snacks. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 10 EgoChaser Snacks. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 5 Pißwasser Drinks. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 5 eCola Drinks. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Pack of Redwood. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 500XP. \n Your XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got clothing <:clothing:839192909583613982>. \n You can spin the wheel again in 3h.",
               #f"{ctx.author.mention} spinned the Lucky Wheel and got arrested by the FBI <a:FlashingWanted:839193592999444520>. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got a slap <a:Slap:839192442199867422>. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 100XP. \n Your XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 50XP. \n XP will be awarded within 3h.  \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got champagne <:TomConnors:839192145482612776>. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got nothing, get trolled <:GTASeriesVideos:839162693415206962>. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 2kRP <:Kapp:839190045767630899>. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Ghost Organization <:CoolBread:839191670767616011> \n You are now hidden from other users. \n To use this, please ask an operator to add the role to you. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 7500XP <:FennPOG:839189820668248135>. \n Your XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 70XP. \n Your XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and hit the Jackpot and got 20,000XP <:FennPOG:839189820668248135>. \n XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got a bonk on the head <a:Bonk:839190543095169055>. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got bread <:Bread:839190517555265606>. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 1XP. XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               #f"{ctx.author.mention} spinned the Lucky Wheel and hit the Fucking Jackpot and got 25,000XP <:FennPOG:839189820668248135> \n XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               #f"{ctx.author.mention} spinned the Lucky Wheel and hit the Fucking Fuck Jackpot and got 35,000XP <:FennPOG:839189820668248135> \n XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               #f"{ctx.author.mention} spinned the Lucky Wheel and hit the Fucking Fucker Fuck Jackpot and got 50,000XP <:FennPOG:839189820668248135> \n XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               #f"{ctx.author.mention} spinned the Lucky Wheel and got the podium vehicle. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got $50,000 \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 10% Vehicle Discount <:Kapp:839190045767630899> \n You can spin the wheel again in 3h.",
               #f"{ctx.author.mention} spinned the Lucky Wheel and got Full Ammo \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and go- *an unknown has placed a $9000 bounty on you!* <:mmmonkas:876174042044981289> \n You can spin the wheel again in 3h.",
               #f"{ctx.author.mention} spinned the Lucky Wheel and got 25.000 Chips. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 5 Taco :taco: \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 10 Taco :taco: \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got A Random Special Cargo Item. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got All Snacks Replenished. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Resupplied Bunker. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 5,000 XP <:FennPOG:839189820668248135> \n XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 10,000 XP <:FennPOG:839189820668248135> \n XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 20,000 XP <:FennPOG:839189820668248135> \n XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
               ]
        if ctx.channel.id == bot_channel:
            await ctx.send(f'{random.choice(ans)}')

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

    @wheelspin.error  # command name error
    async def wheelspin_error(self, ctx, error):  # define error
        # tells the bot its a cool down error
        if isinstance(error, commands.CommandOnCooldown):
            # msg is the message you would like to send, the format is how it formats the seconds left.
            cd = round(error.retry_after)
            if cd == 0:
                cd = 1
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.name}**, you need to wait {self.better_time(cd)} to use that command again.")
        await ctx.send(embed=embed)  # sends the error message to the channel


def setup(client):
    client.add_cog(wheelspin(client))

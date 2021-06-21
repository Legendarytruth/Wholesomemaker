import discord
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp
import random
from discord.ext.commands import cooldown, BucketType

bot_channel = 808958457855344640


class wheelspin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 21600, commands.BucketType.user)
    async def wheelspin(self, ctx):
        ans = [f"{ctx.author.mention} spinned the Lucky Wheel and got 10 P’s & Q’s Snacks. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 10 Meteorite Snacks. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 10 EgoChaser Snacks. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 5 Pißwasser Drinks. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 5 eCola Drinks. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Pack of Redwood. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 10 P’s & Q’s Snacks. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 500XP. \n Your XP will be awarded within 6h. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got clothing <:clothing:839192909583613982>. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got arrested by the FBI <a:FlashingWanted:839193592999444520>. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got a slap <a:Slap:839192442199867422>. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 100XP. \n Your XP will be awarded within 6h. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 50XP. \n XP will be awarded within 6h.  \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got champagne <:TomConnors:839192145482612776>. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got nothing, get trolled <:GTASeriesVideos:839162693415206962>. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 2kRP <:Kapp:839190045767630899>. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Ghost Organization <:CoolBread:839191670767616011> \n You are now hidden from other users. \n To use this, please ask an operator to add the role to you. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 7500XP <:FennPOG:839189820668248135>. \n Your XP will be awarded within 6h. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 70XP. \n Your XP will be awarded within 6h. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and hit the Jackpot and got 20,000XP <:FennPOG:839189820668248135>. \n XP will be awarded within 6h. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got a bonk on the head <a:Bonk:839190543095169055>. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got bread <:Bread:839190517555265606>. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 1XP. XP will be awarded within 6h. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got the podium vehicle + 5,000XP <:CoolBread:839191670767616011>. \n XP will be awarded within 6h. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got the podium vehicle. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got $50,000 \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Mystery Spin <:CoolBread:839191670767616011> \n To use this, please ask an operator to spin the Mystery Spin. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 10% Vehicle Discount <:Kapp:839190045767630899> \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Full Ammo \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got $25,000. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 5 eCola Drinks. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got 25.000 Chips. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got A Random Special Cargo Item. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got All Snacks Replenished. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Resupplied Bunker. \n You can spin the wheel again in 6h.",
               f"{ctx.author.mention} spinned the Lucky Wheel and got Mystery Spin + 5,000 XP <:CoolBread:839191670767616011> \n To use this, please ask an operator to spin the Mystery Spin. \n XP will be awarded within 6h. \n You can spin the wheel again in 6h."
               ]
        if ctx.channel.id == bot_channel:
            #embed = discord.Embed(colour=discord.Colour.green())
            # embed = discord.Embed(
            #    description=f'{random.choice(ans)}', colour=discord.Colour.green())
            # embed.set_footer(
            #    text=f"Credits to ZappiestSet81#1999 for the Responses, Love you Homie! ❤️", icon_url="https://cdn.discordapp.com/attachments/826162439799308350/832703090939265024/pet.gif")
            await ctx.reply(f'{random.choice(ans)}', mention_author=False)
        # else:
            # embed = discord.Embed(
            #    description=f"<:cross:839158779815657512> **{ctx.author.name}** that command is disabled in this channel.")
            # await ctx.channel.send(embed=embed)

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
                description=f"<:cross:839158779815657512> **{ctx.author.name}** you need to wait {self.better_time(cd)} to use that command again.")
        await ctx.send(embed=embed)  # sends the error message to the channel


def setup(client):
    client.add_cog(wheelspin(client))

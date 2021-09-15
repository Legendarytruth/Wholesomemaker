import discord
import discord_slash.cog_ext
from discord.ext import commands
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from discord.ext.commands import cooldown, BucketType
from discord_slash import *
from discord_slash.utils.manage_commands import create_option

load_dotenv()

cluster = MongoClient(os.getenv("MONGODB_URL"))


warning = cluster["discord"]["warning"]
mute = cluster["discord"]["muted"]
kicks = cluster["discord"]["kicks"]

talk_channels = [818815530647158784, 818815613266952193, 808958457855344640, 837680350716362814, 815213963871911996, 828968512146898954, 839444297542533140, 825272629559951390,
                 826078465781661736, 826078419888242708, 837720268918882305, 837665514654138480, 829866889937289257, 824809146641154130, 834312211454754826, 834312245571747842,
                 817712543795249182, 816763959931043861]

bot_channel = 808958457855344640


class warnsys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channels:
            stats = warning.find_one({"id": message.author.id})
            mutes = mute.find_one({"id": message.author.id})
            kicked = kicks.find_one({"id": message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id": message.author.id,
                               "warncount": 0, "reason": 0}
                    warning.insert_one(newuser)
                if mutes is None:
                    newuser = {"id": message.author.id,
                               "mutecount": 0, "reason": 0}
                    mute.insert_one(newuser)
                if kicked is None:
                    newuser = {"id": message.author.id,
                               "kickcount": 0, "reason": 0}
                    kicks.insert_one(newuser)

    @cog_ext.cog_slash(name="warn",
                       description="Give a User some Warnings.",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person Wants to be Warned?",
                               option_type=6,
                               required=True
                           ),
                           create_option(
                               name="reason",
                               description="Provide the reason.",
                               option_type=3,
                               required=False
                           )
                       ])
    @commands.has_role(825578057498099732)
    async def warn(self, ctx: SlashContext, member: discord.Member = None, *, reason: str = None):

        if reason is None:
            reason = ("No Reason Provided.")

        if member == 351147060956889088:
            ctx.send(
                f"<:cross:839158779815657512> {ctx.author} You can't warn Server Owner.", hidden=True)

        stats = warning.find_one({"id": member.id})
        if stats is None:
            warning.insert_one(
                {"id": member.id, "warncount": 1, "reason": reason})
            channel = self.client.get_channel(831215570631393392)
            embed = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** warns **{member.mention}** for following reason : {reason}", colour=discord.Colour.green())
            await channel.send(embed=embed)
            await member.send(f'You have been warned on **{ctx.guild}** for the following reason: {reason}')
            await ctx.send(f'**{member.mention}** has been warned for the following reason: {reason}', hidden=True)
        else:
            warncount = stats["warncount"] + 1
            warning.update_one({"id": member.id}, {"$set": {
                "warncount": warncount, "reason": reason}})
            channel = self.client.get_channel(831215570631393392)
            embed = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** warns **{member.mention}** for following reason : {reason}", colour=discord.Colour.green())
            await channel.send(embed=embed)
            await member.send(f'You have been warned on **{ctx.guild}** for the following reason: {reason}')
            await ctx.send(f'**{member.mention}** has been warned for the following reason: {reason}', hidden=True)

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&825578057498099732> roles to use this command!")
            await ctx.channel.send(embed=embed, hidden=True)

    @cog_ext.cog_slash(name="resetwarn",
                       description="Reset this User Warnings.",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person?",
                               option_type=6,
                               required=False
                           )])
    @commands.has_role(823029389154844743)
    async def resetwarn(self, ctx: SlashContext, *, member: discord.Member = None):

        if member is None:
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.name}**, you can't reset your own Warnings!", colour=discord.Colour.red())
            await ctx.send(embed=embed, hidden=True)
        else:
            # if ctx.channel.id == botcommands_channel:
            warning.delete_one({"id": member.id})
            channel = self.client.get_channel(831215570631393392)
            embed = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** reset **{member.mention}** warnings.", colour=discord.Colour.green())
            await channel.send(embed=embed)
            embed = discord.Embed(
                description=f"<:check:839158727512293406>  **{member.name}**'s Warnings has been resetted.", colour=discord.Colour.green())
            await ctx.send(embed=embed, hidden=True)

    @resetwarn.error
    async def resetwarn_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&823029389154844743> roles to use this command!")
            await ctx.send(embed=embed, hidden=True)

    @cog_ext.cog_slash(name="warnings", description="Know your warnings.")
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def warnings(self, ctx: SlashContext):
        if ctx.channel.id == bot_channel:
            stats = warning.find_one({"id": ctx.author.id})
            mutes = mute.find_one({"id": ctx.author.id})
            kicked = kicks.find_one({"id": ctx.author.id})
            embed = discord.Embed(
                title="{}'s Warnings".format(ctx.author.name), colour=discord.Colour.dark_purple())
            embed.add_field(
                name=":pushpin: Warnings", value="_ _", inline=False)
            embed.add_field(
                name="Warn Count", value=stats["warncount"], inline=False)
            embed.add_field(
                name="Latest Reason", value=stats["reason"], inline=False)
            embed.add_field(
                name=":pushpin: Mutes", value="_ _", inline=False)
            embed.add_field(
                name="Mute Count", value=mutes["mutecount"], inline=False)
            embed.add_field(
                name="Latest Reason", value=mutes["reason"], inline=False)
            embed.add_field(
                name=":pushpin: Kicks", value="_ _", inline=False)
            embed.add_field(
                name="Kick Count", value=kicked["kickcount"], inline=False)
            embed.add_field(
                name="Latest Reason", value=kicked["reason"], inline=False)
            # embed.add_field(
            #    name=":pushpin: Bans", value="> If you're feeling getting a softban, Please Appeal it [Here](https://gnztmpz.eu.org)", inline=False)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.author.send(embed=embed)
            await ctx.send("I have DM'ed you with your Warning List. You can see your warnings again in 24h.", hidden=True)
        else:
            return await ctx.send(f"<:cross:839158779815657512> **{ctx.author.mention}**, that command is disabled in this channel.")

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

    @warnings.error  # command name error
    async def warnings_error(self, ctx, error):  # define error
        # tells the bot its a cool down error
        if isinstance(error, commands.CommandOnCooldown):
            # msg is the message you would like to send, the format is how it formats the seconds left.
            cd = round(error.retry_after)
            if cd == 0:
                cd = 1
            # msg is the message you would like to send, the format is how it formats the seconds left.
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.name}**, you need to wait {self.better_time(cd)} to use that command again.", colour=discord.Colour.red())
            # sends the error message to the channel
            await ctx.send(embed=embed, hidden=True)


def setup(client):
    client.add_cog(warnsys(client))

import discord
from discord.ext import commands
from pymongo import MongoClient
from discord.ext.commands import cooldown, BucketType

bot_channel = 812211967095472149
botcommands_channel = 808958457855344640
talk_channels = [818815530647158784, 818815613266952193, 808958457855344640, 837680350716362814, 815213963871911996, 828968512146898954, 839444297542533140, 825272629559951390,
                 826078465781661736, 826078419888242708, 837720268918882305, 837665514654138480, 829866889937289257, 824809146641154130, 834312211454754826, 834312245571747842,
                 817712543795249182, 816763959931043861, 854740829192060978]

level = ["Thug", "Hustler", "Soldier", "Trigger", "Enforcer",
         "Facilitator", "Public Enemy", "Shot Caller", "Street Boss", "Kingpin"]
levelnum = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

cluster = MongoClient(
    "your mongodb databases")

levelling = cluster["discord"]["levelling"]


class levelsys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channels:
            stats = levelling.find_one({"id": message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id": message.author.id,
                               "xp": 100, "username": message.author.name, "discrim": message.author.discriminator, "messagecount": 1}
                    levelling.insert_one(newuser)
                else:
                    xp = stats["xp"] + 5
                    kung = stats["messagecount"] + 1
                    levelling.update_one({"id": message.author.id}, {
                                         "$set": {"xp": xp, "username": message.author.name, "discrim": message.author.discriminator, "messagecount": kung}})
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*lvl)):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    if xp == 0:
                        channel = self.client.get_channel(812211967095472149)
                        await channel.send(f"Congratulations, {message.author.mention}. You've reached **level {lvl}** .")
                    for i in range(len(level)):
                        if lvl == levelnum[i]:
                            await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))

    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def rank(self, ctx, *, member:  discord.Member = None):

        if member is None:
            member = ctx.author

        if ctx.channel.id == bot_channel:
            stats = levelling.find_one({"id": member.id})
            if stats is None:
                embed = discord.Embed(
                    description=f"<:cross:839158779815657512> **{member.name}** aren't ranked yet. Send some messages first, then try again.", colour=discord.Colour.red())
                await ctx.channel.send(embed=embed)
            else:
                xp = stats["xp"]
                exp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                    if xp < ((50*(lvl**2))+(50*lvl)):
                        break
                    lvl += 1
                xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                boxes = int((xp/(200*((1/2) * lvl)))*20)
                rankings = levelling.find().sort("xp", -1)
                for x in rankings:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                embed = discord.Embed(
                    title="{}'s level stats".format(member.name), colour=discord.Colour.dark_purple())
                embed.add_field(
                    name="Name", value=member.mention, inline=True)
                embed.add_field(
                    name="Experience", value=f"{exp} XP", inline=False)
                embed.add_field(
                    name="Rank", value=f"#{rank}", inline=True)
                embed.add_field(
                    name="Level", value=f"{lvl}", inline=True)
                embed.add_field(name=f"[{xp}/{int(200*((1/2)*lvl))} XP]", value=boxes * "■" + (
                    20-boxes) * "□", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(
                    text=f"No XP Farming Allowed!", icon_url="https://cdn.discordapp.com/emojis/763400376409915406.png?v=1")
                await ctx.channel.send(embed=embed)
        else:
            return await ctx.send(f"<:cross:839158779815657512> **{member.name}**, that command is disabled in this channel.")

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

    @rank.error  # command name error
    async def rank_error(self, ctx, error):  # define error
        # tells the bot its a cool down error
        if isinstance(error, commands.CommandOnCooldown):
            # msg is the message you would like to send, the format is how it formats the seconds left.
            cd = round(error.retry_after)
            if cd == 0:
                cd = 1
            # msg is the message you would like to send, the format is how it formats the seconds left.
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.name}** you need to wait {self.better_time(cd)} to use that command again.", colour=discord.Colour.red())
        await ctx.send(embed=embed)  # sends the error message to the channel

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def givexp(self, ctx, member: discord.Member = None, *, exp: int):

        if member is None:
            member = ctx.author

        stats = levelling.find_one({"id": member.id})
        xp = stats["xp"] + exp
        # if ctx.channel.id == botcommands_channel
        levelling.update_one({"id": member.id}, {"$set": {
            "xp": xp, "username": member.name, "discrim": member.discriminator}})
        embed = discord.Embed(
            description=f"<:check:839158727512293406> {exp} XP has been given to **{member.name}**", colour=discord.Colour.green())
        await ctx.channel.send(embed=embed)
        # \n Now, {member.name} Currently have {exp} XP.
        # else:
        #    await ctx.send(f"<:cross:839158779815657512> **{ctx.author.name}**, that command is disabled in this channel.")

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def resetxp(self, ctx, *, member: discord.Member = None):

        if member is None:
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.name}**, you can't reset your own XP! \n Please provide the UserID/Tag.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            # if ctx.channel.id == botcommands_channel:
            levelling.delete_one({"id": member.id})
            embed = discord.Embed(
                description=f"<:check:839158727512293406>  **{member.name}**'s XP has been resetted.", colour=discord.Colour.green())
            await ctx.channel.send(embed=embed)
            # \n Now, {member.name} Currently have {exp} XP.
        # else:
        #    await ctx.send(f"<:cross:839158779815657512> **{ctx.author.name}**, that command is disabled in this channel.")

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def setxp(self, ctx, member: discord.Member = None, *, exp: int):

        if member is None:
            member = ctx.author

        stats = levelling.find_one({"id": member.id})
        # if ctx.channel.id == botcommands_channel:
        levelling.update_one({"id": member.id}, {"$set": {
            "xp": exp, "username": member.name, "discrim": member.discriminator}})
        embed = discord.Embed(
            description=f"<:check:839158727512293406> **{member.name}**'s XP has been set to {exp} XP.", colour=discord.Colour.green())
        await ctx.channel.send(embed=embed)
        # \n Now, {member.name} Currently have {exp} XP.
        # else:
        #    await ctx.send(f"<:cross:839158779815657512> **{ctx.author.name}**, that command is disabled in this channel.")

    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def levels(self, ctx):
        if (ctx.channel.id == bot_channel):
            rankings = levelling.find().sort("xp", -1)
            mescount = levelling.find().sort("messagecount", -1)
            i = 1
            embed = discord.Embed(
                title=f"{ctx.guild.name}'s Leaderboards", colour=discord.Colour.blurple())
            for x in rankings:
                try:
                    icon = str(ctx.guild.icon_url)
                    temp = await ctx.guild.fetch_member(x["id"])
                    tempxp = x["xp"]
                    msgcount = x["messagecount"]
                    embed.set_thumbnail(url=icon)
                    embed.add_field(name=f"{i}. `{temp}`",
                                    value=f"Experience: {tempxp}xp | Message: {msgcount}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
            embed.add_field(name=f"Role Rewards",
                            value=f"<@&812176809852141569>, <@&812213398351118366>, <@&812214255432106005>, <@&812215368663826442>, <@&812215661824049213>, <@&847144224260358214>, <@&847144504535679076>, <@&847144667136655410>, <@&847144638430183495>, <@&812215772935749633>", inline=False)
            embed.add_field(name=f"* A Quick Sidenote:",
                            value=f"Please contact <@&825578057498099732> regardless of Doubling Levelling Roles. Thanks.", inline=False)
            embed.add_field(name=f"How it Works",
                            value=f"Every minute that you're messaging, you randomly gain between 5 and 20 XP. \n To avoid spamming, earning XP is limited to once a minute per user. \n In <#812211967095472149>, you can type !rank to see your rank and level.", inline=False)
            embed.set_footer(text=f"No XP Farming Allowed!",
                             icon_url="https://cdn.discordapp.com/emojis/763400376409915406.png?v=1")
            await ctx.channel.send(embed=embed)
        else:
            await ctx.send(f"<:cross:839158779815657512> **{ctx.member.name}**, that command is disabled in this channel.")

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

    @levels.error  # command name error
    async def levels_error(self, ctx, error):  # define error
        # tells the bot its a cool down error
        if isinstance(error, commands.CommandOnCooldown):
            # msg is the message you would like to send, the format is how it formats the seconds left.
            cd = round(error.retry_after)
            if cd == 0:
                cd = 1
            # msg is the message you would like to send, the format is how it formats the seconds left.
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.name}** you need to wait {self.better_time(cd)} to use that command again.", colour=discord.Colour.red())
        await ctx.send(embed=embed)  # sends the error message to the channel


def setup(client):
    client.add_cog(levelsys(client))

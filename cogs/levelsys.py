import discord
import discord_slash.cog_ext
from discord.ext import commands
from pymongo import MongoClient
from discord.ext.commands import cooldown, BucketType
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
from discord_slash.utils.manage_components import create_button, create_actionrow

bot_channel = 812211967095472149
botcommands_channel = 808958457855344640
talk_channels = [812211967095472149, 825248166713622548, 866608473964544010, 866608518365708298, 812170448124510220, 817385869627097128, 807476822111420416, 830222254942978069, 824091824540614706, 857649456145235978, 806964929718255619, 818815530647158784, 808958457855344640,
                 826078465781661736, 826078419888242708, 818815613266952193, 839444297542533140, 837680350716362814, 829866889937289257, 823152070189383700, 851398046951669770, 849008568178180137, 823573307215052830, 849130878701010965, 834312211454754826, 834312245571747842]

talk_channels_noadmin = [812211967095472149, 825248166713622548, 812170448124510220, 817385869627097128, 807476822111420416, 830222254942978069, 824091824540614706, 857649456145235978, 806964929718255619, 818815530647158784, 808958457855344640,
                         826078465781661736, 826078419888242708, 818815613266952193, 839444297542533140, 837680350716362814, 829866889937289257, 823152070189383700, 851398046951669770, 849008568178180137, 823573307215052830, 849130878701010965, 834312211454754826, 834312245571747842]


# role rewards
level = ["Thug", "Hustler", "Soldier", "Trigger", "Enforcer",
         "Facilitator", "Public Enemy", "Shot Caller", "Street Boss", "Right Hand", "Kingpin"]

# role rewards count
levelnum = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

cluster = MongoClient(
    "your mongodb uri")

levelling = cluster["discord"]["levelling"]

logging = cluster["discord"]["logging"]


class levelsys(commands.Cog):
    def __init__(self, client):
        self.client = client
# this cog.listener is to log all people level count, based on sending a message. there is no problem at all.. move along folks :)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        stats = logging.find_one({"id": before.author.id})
        imgp = str(before.author.avatar_url)
        logging.update_one({"message_id": before.id}, {"$set": {"username": before.author.name, "discrim": before.author.discriminator, "image_url": imgp, "message": str(
            before.content), "editedto": str(after.content), "messageat": str(before.created_at), "editedat": str(after.created_at), "user_id": before.author.id}})

        if before.channel.id in talk_channels_noadmin:
            channel = self.client.get_channel(831215570631393392)
            embed = discord.Embed(
                description=f"**Message Edited in <#{before.channel.id}>**", colour=discord.Colour.dark_green())
            embed.set_author(name=f'{before.author}',
                             icon_url=before.author.avatar_url)
            embed.add_field(name=f"Before:",
                            value=f"{before.content}", inline=False)
            embed.add_field(name=f"After:",
                            value=f"{after.content}", inline=False)
            embed.set_footer(
                text=f"Message ID: {after.id} • User ID: {before.author.id}")

        button = create_button(5, label='Jump to Message',
                               url=f'{after.jump_url}')
        await channel.send(embed=embed, components=[create_actionrow(button)])

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.channel.id in talk_channels_noadmin:
            channel = self.client.get_channel(831215570631393392)
            embed = discord.Embed(
                description=f"**Message sent by {message.author} deleted in <#{message.channel.id}>**", colour=discord.Colour.red())
            embed.set_author(name=f'{message.author}',
                             icon_url=message.author.avatar_url)
            embed.add_field(name=f"Message:",
                            value=f"{message.content}", inline=False)
            embed.set_footer(
                text=f"Author: {message.author.id} • Message ID: {message.id}")
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channels_noadmin:
            stats = levelling.find_one({"id": message.author.id})
            imgp = str(message.author.avatar_url)

            newuser = {"id": message.id, "username": message.author.name, "discrim": message.author.discriminator, "image_url": imgp, "message": str(
                message.content), "messageat": str(message.created_at), "user_id": message.author.id}
            logging.insert_one(newuser)

            if not message.author.bot:
                if stats is None:
                    newuser = {"id": message.author.id,
                               "xp": 100, "username": message.author.name, "discrim": message.author.discriminator, "messagecount": 1, "image_url": imgp}
                    levelling.insert_one(newuser)

                else:
                    xp = stats["xp"] + 5
                    kung = stats["messagecount"] + 1
                    img = str(message.author.avatar_url)
                    levelling.update_one({"id": message.author.id}, {
                                         "$set": {"xp": xp, "username": message.author.name, "discrim": message.author.discriminator, "messagecount": kung, "image_url": img}})
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

    @cog_ext.cog_slash(name="rank",
                       description="Know your or someone Rank.",
                       options=[
                           create_option(
                               name="member",
                               description="Sees this User Rank.",
                               option_type=6,
                               required=False
                           )
                       ])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def rank(self, ctx: SlashContext, *, member:  discord.Member = None):

        if member is None:
            member = ctx.author

        if ctx.channel.id == bot_channel:
            stats = levelling.find_one({"id": member.id})
            if stats is None:
                embed = discord.Embed(
                    description=f"<:cross:839158779815657512> **{member.name}** aren't ranked yet. Send some messages first, then try again.", colour=discord.Colour.red())
                await ctx.send(embed=embed)
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
                await ctx.send(embed=embed)
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

    @cog_ext.cog_slash(name="givexp",
                       description="Give you or this User some XP Rewards.",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person Receive this XP?",
                               option_type=6,
                               required=True
                           ),
                           create_option(
                               name="exp",
                               description="How Many XP Should I Give?",
                               option_type=4,
                               required=True
                           )
                       ])
    @commands.has_role(845586428057354253)  # dispatch role (head moderators)
    async def givexp(self, ctx: SlashContext, member: discord.Member, *, exp: int):

        stats = levelling.find_one({"id": member.id})
        xp = stats["xp"] + exp
        # if ctx.channel.id == botcommands_channel
        levelling.update_one({"id": member.id}, {"$set": {
            "xp": xp, "username": member.name, "discrim": member.discriminator}})
        embed = discord.Embed(
            description=f"<:check:839158727512293406> {exp} XP has been given to **{member.name}**", colour=discord.Colour.green())
        await ctx.send(embed=embed)
        # \n Now, {member.name} Currently have {exp} XP.
        # else:
        #    await ctx.send(f"<:cross:839158779815657512> **{ctx.author.name}**, that command is disabled in this channel.")

    @givexp.error
    async def givexp_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&845586428057354253> roles to use this command!")
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="resetxp",
                       description="Reset this User XP.",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person?",
                               option_type=6,
                               required=True
                           )])
    @commands.has_role(823029389154844743)  # dispatch role (head moderators)
    async def resetxp(self, ctx: SlashContext, *, member: discord.Member):

        levelling.delete_one({"id": member.id})
        embed = discord.Embed(
            description=f"<:check:839158727512293406>  **{member.name}**'s XP has been resetted.", colour=discord.Colour.green())
        await ctx.send(embed=embed)

    @resetxp.error
    async def resetxp_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&823029389154844743> roles to use this command!")
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="setxp",
                       description="Set you or this User XP.",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person Should I Set?",
                               option_type=6,
                               required=True
                           ),
                           create_option(
                               name="exp",
                               description="How Many XP Should I Set?",
                               option_type=4,
                               required=True
                           )
                       ])
    @commands.has_role(823029389154844743)  # dispatch role (head moderators)
    async def setxp(self, ctx: SlashContext, member: discord.Member, *, exp: int):

        stats = levelling.find_one({"id": member.id})
        # if ctx.channel.id == botcommands_channel:
        levelling.update_one({"id": member.id}, {"$set": {
            "xp": exp, "username": member.name, "discrim": member.discriminator}})
        embed = discord.Embed(
            description=f"<:check:839158727512293406> **{member.name}**'s XP has been set to {exp} XP.", colour=discord.Colour.green())
        await ctx.send(embed=embed)

    @setxp.error
    async def setxp_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&823029389154844743> roles to use this command!")
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="levels", description="Receive Wholesome Series Videos Leaderboard.")
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def levels(self, ctx: SlashContext):
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
                            value=f"Level 1 : <@&812176809852141569> \n Level 5 : <@&812213398351118366> \n Level 10 : <@&812214255432106005> \n Level 15 : <@&812215368663826442> \n Level 20 : <@&812215661824049213> \n Level 25 : <@&847144224260358214> \n Level 30 : <@&847144504535679076> \n Level 35 : <@&847144667136655410> \n Level 40 : <@&847144638430183495> \n Level 45 : <@&863946146165817344> \n Level 50 : <@&812215772935749633>", inline=False)
            embed.add_field(name=f"* A Quick Sidenote:",
                            value=f"The role is given by the bot automatically and it **will** stack up with the previous one. If you find yourself with two or more of these roles, please contact a <@&825578057498099732> to fix it or the bot might not be able to level you up correctly. Thanks.", inline=False)
            embed.add_field(name=f"How it Works",
                            value=f"Every minute that you're messaging, you randomly gain between 5 and 20 XP. \n To avoid spamming, earning XP is limited to once a minute per user. \n In <#812211967095472149>, you can type `/rank` to see your rank and level.", inline=False)
            embed.set_footer(text=f"No XP Farming Allowed!",
                             icon_url="https://cdn.discordapp.com/emojis/763400376409915406.png?v=1")
            await ctx.send(embed=embed)
        else:
            return await ctx.send(f"<:cross:839158779815657512> **{ctx.member.name}**, that command is disabled in this channel.")

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

import os
import random
import discord
from discord import Embed
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle


class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="help", description="Shows the Help Commands Menu.",
                       options=[
                           create_option(
                               name="category",
                               description="Please Provide the Help Category.",
                               option_type=3,
                               required=False
                           )
                       ])
    async def help(self, ctx: SlashContext, category: str = None):
        if category is None:
            embed = discord.Embed(
                colour=discord.Colour.magenta()
            )

            embed.set_author(
                name='Samantha, The Wholesome Series Videos Discord Bot')
            embed.set_thumbnail(
                url="https://raw.githubusercontent.com/GNZTMPZ/Samantha/main/sam.png")
            embed.add_field(
                name='_ _', value='_Use [`/`] help [command name] to see more info on a command._', inline=False)
            # embed.add_field(
            #    name='**Featured Commands**', value='`Say hello, Sam` (on canary mode, not yet finished)', inline=False)
            embed.add_field(name='**Fun commands**',
                            value='pat, hug, kill, kiss, neko, smug, sad, slap, meme, dog', inline=False)
            embed.add_field(name='**Economic commands**',
                            value='rank, levels, wheelspin', inline=False)
            embed.add_field(name='**Server Related commands**',
                            value='invite, rules, roles, links, warnings', inline=False)
            embed.add_field(name='**Misc commands**',
                            value='help, avatar, ping, serverinfo, userinfo, bigemote', inline=False)
            embed.add_field(name='**Moderation commands**',
                            value='kick, ban, unban, slowmode, mute, unmute, prune, mysteryspin, givexp, resetxp, setxp, warn, resetwarn', inline=False)
            embed.add_field(name='**Samantha s̶i̶m̶p config man commands**',
                            value='shutdown, reboot', inline=False)
            embed.add_field(name='_ _',
                            value='... _and more, will you be able to find them all?_', inline=False)
            embed.add_field(name='Also, Did you know?',
                            value='Samantha is **Open Source!** *yay!, poggers!* \n You can check it out at this [Github Repository](https://github.com/GNZTMPZ/Samantha). \n Want to Contribute? Feel free to check out this [Github Issues](https://github.com/GNZTMPZ/Samantha/issues/2) for more info! :grin:', inline=False)
            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

            button = create_button(5, label='Github Repository',
                                   url='https://github.com/GNZTMPZ/Samantha')
            button2 = create_button(
                5, label='Github Issues', url='https://github.com/GNZTMPZ/Samantha/issues/2')

            return await ctx.send(embed=embed, components=[create_actionrow(button), create_actionrow(button2)])

        if category == "ping":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Ping Command__',
                            value='See the bots latency.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/ping', inline=False)

            return await ctx.send(embed=embed)

        if category == "avatar":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Avatar Command__',
                            value='See your/other people avatar.', inline=False)
            embed.add_field(name='__Aliases:__', value='avatar', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/avatar <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "serverinfo":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Serverinfo Command__',
                            value='See `This Server` statistics.', inline=False)
            embed.add_field(name='__Aliases:__', value='si', inline=False)
            embed.add_field(name='__How to use:__',
                            value='!serverinfo', inline=False)

            return await ctx.send(embed=embed)

        if category == "userinfo":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Userinfo Command__',
                            value='See your/other people user info.', inline=False)
            embed.add_field(name='__Aliases:__', value='ui', inline=False)
            embed.add_field(name='__How to use:__',
                            value='!userinfo <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "bigemote":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Big Emote Command__',
                            value="as the name says, it's for emoji resizer.", inline=False)
            embed.add_field(name='__Aliases:__',
                            value='bigemoji, be', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/bigemote <emote>', inline=False)

            return await ctx.send(embed=embed)

        if category == "kick":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Kick Command__',
                            value='Kick Somebody out from this server.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/kick <userid/tag> <reason>', inline=False)

        return await ctx.send(embed=embed)

        if category == "ban":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Ban Command__',
                            value='Ban Somebody out from this server.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/ban <userid/tag> <reason>', inline=False)

        return await ctx.send(embed=embed)

        if category == "slowmode":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Slowmode Command__',
                            value='Slowing the chats.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/slowmode <time(s/m/h)>', inline=False)

            return await ctx.send(embed=embed)

        if category == "mute":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Mute Command__',
                            value='Mute Somebody on this server.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/mute <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "unmute":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Unmute Command__',
                            value='Unmute Somebody on this server.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/unmute <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "prune":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Prune Command__',
                            value='Cleaning the chats.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/prune <how many messages>', inline=False)

            return await ctx.send(embed=embed)

        if category == "mysteryspin":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Mystery Spin Command__',
                            value="Same with the Wheelspin Commands, but this is more `boom'in` Prize. \n To use this, You must get the Mystery Spin Access from Lucky Wheel. \n Only <@&825578057498099732> can use this commands.", inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/mysteryspin <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "rules":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Rules Command__',
                            value='*Shortcut to* <#828959702029041664> *for those who might need a refresher*', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/rules <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "invite":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Invite Command__',
                            value="*Receive Wholesome Series Videos Discord Invite*", inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/invite', inline=False)

            return await ctx.send(embed=embed)

        if category == "links":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Links Command__',
                            value='*Shortcut to* <#824463250980339755>', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/links <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "warnings":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Warnings Command__',
                            value='Receive a DM from Samantha with the list of your warnings on this server.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/warnings', inline=False)

            return await ctx.send(embed=embed)

        if category == "levels":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Leaderboard Command__',
                            value='Receive Wholesome Series Videos Leaderboards', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/levels', inline=False)

            return await ctx.send(embed=embed)

        if category == "rank":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Rank Command__',
                            value='*See your current rank', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/rank <userid/tag> (optional)', inline=False)

            return await ctx.send(embed=embed)

        if category == "wheelspin":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Wheelspin Command__',
                            value='*This command is like the wheel in GTA. You can use it every 24 hours. \nSimply type the command and the bot will give you something.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/wheelspin', inline=False)

            return await ctx.send(embed=embed)

        if category == "pat":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Pat Command__',
                            value="Pat Someone with some GIF's", inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/pat <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "hug":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Hug Command__',
                            value="Pat Someone with some GIF's", inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/hug <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "punch":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Punch Command__',
                            value="_rekt_ someone with some GIF's", inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/punch <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "kiss":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Kiss Command__',
                            value="Kiss somebody with some Pics. \n _(No GIF's, because the API being a dick :pensive: )_", inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/kiss <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "neko":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Neko Command__',
                            value="Provide you with some Neko Pics.", inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/neko', inline=False)

            return await ctx.send(embed=embed)

        if category == "smug":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Smug Command__',
                            value="Provide you with some smug pics.", inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/smug', inline=False)

            return await ctx.send(embed=embed)

        if category == "sad":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Sad Command__',
                            value="Provide you with some sad GIF's.", inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/sad', inline=False)

            return await ctx.send(embed=embed)

        if category == "slap":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Slap Command__',
                            value="Slap somebody with some GIF's.", inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/slap <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "meme":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Meme Command__',
                            value='Get some ~~not so~~ fresh meme.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/meme', inline=False)

            return await ctx.send(embed=embed)

        if category == "dog":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__dog Command__',
                            value='Give you some dog picture and dog facts', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/dog', inline=False)

            return await ctx.send(embed=embed)

        if category == "givexp":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Give XP Command__',
                            value='Adding XP to Tagged Members. \n Only <@&845586428057354253> can use this commands.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/givexp <userid/tag> <how many xp>', inline=False)

            return await ctx.send(embed=embed)

        if category == "setxp":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Set XP Command__',
                            value='Set Tagged Members XP. \n Only <@&845586428057354253> can use this commands.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/setxp <userid/tag> <how many xp>', inline=False)

            return await ctx.send(embed=embed)

        if category == "resetxp":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Reset XP Command__',
                            value='Reset Tagged Members XP. \n Only <@&845586428057354253> can use this commands.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/resetxp <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "warn":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Warn Command__',
                            value='Warn a User in this server. \n Only <@&845586428057354253> can use this commands.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/warn <userid/tag> <reason>', inline=False)

            return await ctx.send(embed=embed)

        if category == "resetwarn":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Reset Warnings Command__',
                            value='Reset User Warnings. \n Only <@&845586428057354253> can use this commands.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/resetwarn <userid/tag>', inline=False)

            return await ctx.send(embed=embed)

        if category == "shutdown":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Shutdown Command__',
                            value='Shutdown Sam.py for Maintenance \n Only <@&845497466249412628> can use this commands.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/shutdown', inline=False)

            return await ctx.send(embed=embed)

        if category == "reboot":
            embed = discord.Embed(
                colour=discord.Colour.purple()
            )
            embed.add_field(name='__Reboot Command__',
                            value='Reboot Sam.py On the Fly. \n Only <@&845497466249412628> can use this commands.', inline=False)
            embed.add_field(name='__Aliases:__', value='None', inline=False)
            embed.add_field(name='__How to use:__',
                            value='/reboot', inline=False)

            return await ctx.send(embed=embed)


def setup(client):
    client.add_cog(help(client))

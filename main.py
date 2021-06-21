import sys
import discord
from discord.ext import commands
from discord import Embed
import os
import random
from typing import Optional
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.presences = True
# stable prefixes
client = commands.Bot(command_prefix=['sam ', 'Sam ', '!'])
# testing prefixes
#client = commands.Bot(command_prefix='c!')
client.remove_command("help")


@client.command()
@commands.has_role(845497466249412628)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'<:check:839158727512293406> Loaded **{extension}** Modules.')

    channel = client.get_channel(831215570631393392)
    embed = discord.Embed(
        description=f"<:check:839158727512293406> **{ctx.author.mention}** Load **{extension}** Modules.", colour=discord.Colour.green())
    await channel.send(embed=embed)


@load.error
async def load_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.channel.send(embed=embed)


@client.command()
@commands.has_role(845497466249412628)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'<:check:839158727512293406> Unloaded **{extension}** Modules.')

    channel = client.get_channel(831215570631393392)
    embed = discord.Embed(
        description=f"<:check:839158727512293406> **{ctx.author.mention}** Unload **{extension}** Modules.", colour=discord.Colour.green())
    await channel.send(embed=embed)


@unload.error
async def unload_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.channel.send(embed=embed)


@client.command()
@commands.has_role(845497466249412628)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'<:check:839158727512293406> Reloaded **{extension}** module.')

    channel = client.get_channel(831215570631393392)
    embed = discord.Embed(
        description=f"<:check:839158727512293406> **{ctx.author.mention}** Reload **{extension}** Modules.", colour=discord.Colour.green())
    await channel.send(embed=embed)


@reload.error
async def reload_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.channel.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
@commands.has_role(845497466249412628)
async def shutdown(ctx):
    channel = client.get_channel(831215570631393392)
    embed = discord.Embed(
        description=f":wave: **Sam.py** has been Shutdowned. **Goodbye World!**", colour=discord.Colour.red())
    await channel.send(embed=embed)
    await ctx.bot.close()


@shutdown.error
async def shutdown_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.channel.send(embed=embed)


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


@client.command()
@commands.has_role(845497466249412628)
async def reboot(ctx):
    channel = client.get_channel(831215570631393392)
    embed = discord.Embed(
        description=f":repeat: *Rebooting Sam.py..* **Please Standby...**", colour=discord.Colour.red())
    await channel.send(embed=embed)
    restart_program()


@reboot.error
async def reboot_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.channel.send(embed=embed)

# Command Grouping


@client.group(pass_context=True)
async def commands(ctx):
    if ctx.subcommand_passed is None:
        member = ctx.message

        embed = discord.Embed(
            colour=discord.Colour.magenta()
        )

        embed.set_author(
            name='Samantha, The Wholesome Series Videos Discord Bot', icon_url="https://raw.githubusercontent.com/GNZTMPZ/Samantha/main/sam.png")
        embed.set_thumbnail(
            url="https://raw.githubusercontent.com/GNZTMPZ/Samantha/main/sam.png")
        embed.add_field(
            name='_ _', value='_Use [`sam`, `Sam`, `!`] commands [command name] to see more info on a command._', inline=False)
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
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)


@commands.command()
async def ping(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Ping Command__',
                    value='See the bots latency.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__', value='!ping', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def av(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Avatar Command__',
                    value='See your/other people avatar.', inline=False)
    embed.add_field(name='__Aliases:__', value='avatar', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!av <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def serverinfo(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Serverinfo Command__',
                    value='See `This Server` statistics.', inline=False)
    embed.add_field(name='__Aliases:__', value='si', inline=False)
    embed.add_field(name='__How to use:__', value='!serverinfo', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def userinfo(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Userinfo Command__',
                    value='See your/other people user info.', inline=False)
    embed.add_field(name='__Aliases:__', value='ui', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!userinfo <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def bigemote(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Big Emote Command__',
                    value="as the name says, it's for emoji resizer.", inline=False)
    embed.add_field(name='__Aliases:__', value='bigemoji, be', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!bigemote <emote>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def kick(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Kick Command__',
                    value='Kick Somebody out from this server.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!kick <userid/tag> <reason>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def ban(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Ban Command__',
                    value='Ban Somebody out from this server.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!ban <userid/tag> <reason>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def slowmode(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Slowmode Command__',
                    value='Slowing the chats.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!slowmode <time(s/m/h)>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def mute(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Mute Command__',
                    value='Mute Somebody on this server.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!mute <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def unmute(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Unmute Command__',
                    value='Unmute Somebody on this server.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!unmute <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def prune(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Prune Command__',
                    value='Cleaning the chats.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!prune <how many messages>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def mysteryspin(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Mystery Spin Command__',
                    value="Same with the Wheelspin Commands, but this is more `boom'in` Prize. \n To use this, You must get the Mystery Spin Access from Lucky Wheel. \n Only <@&825578057498099732> can use this commands.", inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!mysteryspin <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def rules(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Rules Command__',
                    value='*Shortcut to* <#828959702029041664> *for those who might need a refresher*', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!rules <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def invite(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Invite Command__',
                    value="*Receive Wholesome Series Videos Discord Invite*", inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!invite', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def links(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Links Command__',
                    value='*Shortcut to* <#824463250980339755>', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!links <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def warnings(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Warnings Command__',
                    value='Receive a DM from Samantha with the list of your warnings on this server.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!warnings', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def levels(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Leaderboard Command__',
                    value='Receive Wholesome Series Videos Leaderboards', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!levels', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def rank(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Rank Command__',
                    value='*See your current rank', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!rank', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def wheelspin(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Wheelspin Command__',
                    value='*This command is like the wheel in GTA. You can use it every 24 hours. \nSimply type the command and the bot will give you something.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!wheelspin', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def pat(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Pat Command__',
                    value="Pat Someone with some GIF's", inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!pat <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def hug(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Hug Command__',
                    value="Pat Someone with some GIF's", inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!hug <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def kill(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Kill Command__',
                    value="_rekt_ someone with some gif's, not killing IRL. \n if you want to kill yourself IRL, better call 911 for your own safety.", inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!kill <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def kiss(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Kiss Command__',
                    value="Kiss somebody with some Pics. \n _(No GIF's, because the API being a dick :pensive: )_", inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!kiss <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def neko(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Neko Command__',
                    value="Provide you with some Neko Pics.", inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!neko', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def smug(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Smug Command__',
                    value="Provide you with some smug pics.", inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!smug', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def sad(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Sad Command__',
                    value="Provide you with some sad GIF's.", inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!sad', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def slap(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Slap Command__',
                    value="Slap somebody with some GIF's.", inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!slap <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def meme(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Meme Command__',
                    value='Get some ~~not so~~ fresh meme.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!meme', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def dog(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__dog Command__',
                    value='Give you some dog picture and dog facts', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!dog', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def help(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Help Command__',
                    value='Displays a list of commands.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!help', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def givexp(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Give XP Command__',
                    value='Adding XP to Tagged Members. \n Only <@&845586428057354253> can use this commands.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!givexp <userid/tag> <how many xp>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def setxp(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Set XP Command__',
                    value='Set Tagged Members XP. \n Only <@&845586428057354253> can use this commands.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!setxp <userid/tag> <how many xp>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def resetxp(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Reset XP Command__',
                    value='Reset Tagged Members XP. \n Only <@&845586428057354253> can use this commands.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!resetxp <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def warn(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Warn Command__',
                    value='Warn a User in this server. \n Only <@&845586428057354253> can use this commands.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!warn <userid/tag> <reason>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def resetwarn(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Reset Warnings Command__',
                    value='Reset User Warnings. \n Only <@&845586428057354253> can use this commands.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!resetwarn <userid/tag>', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def shutdown(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Shutdown Command__',
                    value='Shutdown Sam.py for Maintenance \n Only <@&845497466249412628> can use this commands.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!shutdown', inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def reboot(ctx):
    author = ctx.message

    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.add_field(name='__Reboot Command__',
                    value='Reboot Sam.py On the Fly. \n Only <@&845497466249412628> can use this commands.', inline=False)
    embed.add_field(name='__Aliases:__', value='None', inline=False)
    embed.add_field(name='__How to use:__',
                    value='!reboot', inline=False)

    await ctx.send(embed=embed)
# end of command grouping


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name='Matthew™'))
    print('Bot is ready')
    channel = client.get_channel(831215570631393392)
    # Turn this on/off if wanna go stable
    embed = discord.Embed(
        description=f"<a:WaveBlob:827337423649505300> Hey there, **Sam.py** initialised with version **main**", colour=discord.Colour.green())
    # Turn this on/off if wanna go testing mode
    # embed = discord.Embed(
    #    description=f"<a:WaveBlob:827337423649505300> Hey there, **Sam.py** initialised with version **testing**", colour=discord.Colour.green())
    await channel.send(embed=embed)

# sam normal token
client.run('your bot token here')
# sam test bot token
# client.run('your bot token here')

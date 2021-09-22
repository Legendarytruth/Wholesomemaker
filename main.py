import sys
import discord
from discord.ext import commands
from discord import Embed
import discord.utils
from dotenv import load_dotenv
import os
import datetime
import asyncio
import aiohttp
import random
from discord.ext.commands import cooldown, BucketType
from discord import Intents
from typing import Optional
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext
import logging  # for logging things (on testing mode)

load_dotenv()
intents = discord.Intents().all()
intents.members = True
client = commands.Bot(command_prefix=['/', '!'], intents=intents)
slash = SlashCommand(client, sync_commands=True)
client.remove_command("help")
# adding slash commands

@slash.slash(name="load", description="Load a Module")
@commands.has_role(845497466249412628)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'<:check:839158727512293406> Loaded **{extension}** Modules.')


@load.error
async def load_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.send(embed=embed)


@slash.slash(name="unload", description="Unload a Module")
@commands.has_role(845497466249412628)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'<:check:839158727512293406> Unloaded **{extension}** Modules.')


@unload.error
async def unload_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.send(embed=embed)


@slash.slash(name="reload", description="Reload a Module")
@commands.has_role(845497466249412628)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'<:check:839158727512293406> Reloaded **{extension}** module.')


@reload.error
async def reload_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@slash.slash(name="shutdown", description="Shutdowns the Bot.")
@commands.has_role(845497466249412628)
async def shutdown(ctx):
    await ctx.send(f':wave: The bot has been Shutdowned, Goodbye World.')
    channel = client.get_channel(831215570631393392)
    embed = discord.Embed(
        description=f":wave: **Wholesomemaker** has been Shutdowned. **Goodbye World!**", colour=discord.Colour.red())
    await channel.send(embed=embed)
    await ctx.bot.close()


@shutdown.error
async def shutdown_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.send(embed=embed)


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


@slash.slash(name="reboot", description="Reboot the Bot.")
@commands.has_role(845497466249412628)
async def reboot(ctx):
    await ctx.send(f':wave: The bot has been Rebooting, Please Wait..')
    channel = client.get_channel(831215570631393392)
    embed = discord.Embed(
        description=f":repeat: *Rebooting Wholesomemaker..* **Please Standby...**", colour=discord.Colour.red())
    await channel.send(embed=embed)
    restart_program()


@reboot.error
async def reboot_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.send(embed=embed)

 # Customise the message below to what you want to send new users!
newUserMessage = """
Hi! Welcome to the Wholesome Series Videos official Discord server!
Please read the rules and be respectful.
"""
bot_channel = 808958457855344640 #channel that the bot will write too


#Old member join message
"""
@client.event
async def on_member_join(member):
    # Gets the member role as a `role` object
    role = discord.utils.get(member.server.roles, name="non verified")
    await client.add_roles(member, role)  # Gives the role to the user
    await member.send(newUserMessage)
"""
#When the server icon or name changes.
@client.event
async def on_guild_update(before, after):
    iconmessage = 'The server icon has changed.'
    namemessage = 'The server name has changed'
    bot_c = client.get_channel(bot_channel)
    if(before.icon != after.icon):
        await bot_c.send(iconmessage)
    if(before.name != after.name):
        await bot_c.send(namemessage)

# New member join message
@client.event
async def on_member_join(member):
    message = '{0.mention} has joined the server.'
    bot_c = client.get_channel(bot_channel)
    embed = discord.Embed(title= newUserMessage)
    await member.send(embed=embed)
    await bot_c.send(message.format(member))

# Logging if a user leaves
@client.event
async def on_member_remove(member):
    message = '{0.mention} has left/been kicked from the server.'
    bot_c = client.get_channel(bot_channel)
    await bot_c.send(message.format(member))

# when a channel is deleted (The name auto changes to #deleted-channel)
@client.event
async def on_guild_channel_delete(channel):
    message = '{0.mention} has been deleted from the server.'
    bot_c = client.get_channel(bot_channel)
    await bot_c.send(message.format(channel.name))

# when a channel is created
@client.event
async def on_guild_channel_create(channel):
    message = '{0.mention} has been created from the server.'
    bot_c = client.get_channel(bot_channel)
    await bot_c.send(message.format(channel))

# when a channel name is updated
@client.event
async def on_guild_channel_update(before, after):
    message = '{} has been renamed to {}.'
    bot_c = client.get_channel(bot_channel)
    if(before.name != after.name):
        await bot_c.send(message.format(before.name, after.name))

# These are for private channels

#when a private channel is deleted (The name auto changes to #deleted-channel)
@client.event
async def on_private_channel_delete(channel):
    message = '{} has been deleted from the server.'
    bot_c = client.get_channel(bot_channel)
    await bot_c.send(message.format(channel.name))

#when a private channel is created
@client.event
async def on_private_channel_create(channel):
    message = '{0.mention} has been created from the server.'
    bot_c = client.get_channel(bot_channel)
    await bot_c.send(message.format(channel))

#when a private channel name is updated
@client.event
async def on_private_channel_update(before, after):
    message = '{} has been renamed to {}.'
    bot_c = client.get_channel(bot_channel)
    if(before.name != after.name):
        await bot_c.send(message.format(before.name, after.name))


#when a user has a role added or deleted
@client.event
async def on_member_update(before, after):
    addedRole = '{} has gained the role {}.'
    deletedRole = '{} has lost the role {}.'
    bot_c = client.get_channel(bot_channel)
    if(before.roles != after.roles):
        beforelist = before.roles
        afterlist = after.roles
        if(len(before.roles) > len(after.roles)):
            for i in beforelist:
                 if i not in afterlist:
                    role = i
            await bot_c.send(deletedRole.format(before.name, role.name))
        else:
            for i in afterlist:
                 if i not in beforelist:
                    role = i
            await bot_c.send(addedRole.format(before.name, role.name))


#when a new role is created
@client.event
async def on_guild_role_create(role):
    message = 'The role {0.mention} has been created.'
    bot_c = client.get_channel(bot_channel)
    await bot_c.send(message.format(role))

#when a new role is deleted
@client.event
async def on_guild_role_delete(role):
    message = 'The role {} has been deleted.'
    bot_c = client.get_channel(bot_channel)
    await bot_c.send(message.format(role.name))

#when a new role has its color changed
@client.event
async def on_guild_role_update(before, after):
    message = 'The role {} has changed from {} to {}.'
    bot_c = client.get_channel(bot_channel)
    if(before.color != after.color):
        await bot_c.send(message.format(after.name, before.color, after.color))


@ client.event
async def on_ready():

    # versioning.

    # versioning types.

    # Turn this on/off if wanna go stable
    # version = ("main")
    # Turn this on/off if wanna go testing mode
    # version = ("testing")
    # or simply don't type anything to go undefined mode
    # version = ("")

    version = os.getenv("VERSION")

    if version == "master":
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"Matthew™"))
        channel = client.get_channel(831215570631393392)
        embed = discord.Embed(
            description=f"<a:WaveBlob:827337423649505300> Hey there, **Wholesomemaker** initialised with version **{version}**", colour=discord.Colour.green())
        await channel.send(embed=embed)

    if version == "testing":
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name=version))
        channel = client.get_channel(864214499656466432)
        embed = discord.Embed(
            description=f"<a:WaveBlob:827337423649505300> Hey there, **Wholesomemaker** initialised with version **{version}**", colour=discord.Colour.green())
        await channel.send(embed=embed)
        logging.basicConfig(level=logging.INFO)
        logging.basicConfig(level=logging.WARNING)
        logging.basicConfig(level=logging.ERROR)
        logging.basicConfig(level=logging.CRITICAL)
        logging.basicConfig(level=logging.DEBUG)

    if version == "🕯️ R.I.P. -":
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name=version))
        channel = client.get_channel(831215570631393392)
        embed = discord.Embed(
            description=f"<a:WaveBlob:827337423649505300> Hey there, **Wholesomemaker** initialised with version **{version}**", colour=discord.Colour.green())
        await channel.send(embed=embed)

    if version is None:
        channel = client.get_channel(831215570631393392)
        embed = discord.Embed(
            description=f"<a:WaveBlob:827337423649505300> Hey there, **Wholesomemaker** initialised with version **None**", colour=discord.Colour.green())
        await channel.send(embed=embed)

    print(f"Wholesomemaker is ready for action with version {version}")

client.run(os.getenv("BOT_TOKEN"))

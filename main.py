import sys
import discord
from discord.ext import commands
from discord import Embed
from typing import Optional
import os
import datetime
import asyncio
import aiohttp
import random
from discord.ext.commands import cooldown, BucketType
from typing import Optional
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext
import logging  # for logging things (on testing mode)

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.reactions = True
# stable prefixes
# up to you, the prefix is not used.. cuz we've done slash commands :)
client = commands.Bot(command_prefix=['sam ', 'Sam ', '/'])

# please, don't delete this. this is our main prefix ;)
slash = SlashCommand(client, sync_commands=True)
client.remove_command("help")

# adding slash commands


@slash.slash(name="load", description="Load a Module")
@commands.has_role(845497466249412628)  # Samantha config man roles
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'<:check:839158727512293406> Loaded **{extension}** Modules.')


@load.error
async def load_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.channel.send(embed=embed)


@slash.slash(name="unload", description="Unload a Module")
@commands.has_role(845497466249412628)  # Samantha config man roles
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'<:check:839158727512293406> Unloaded **{extension}** Modules.')


@unload.error
async def unload_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.channel.send(embed=embed)


@slash.slash(name="reload", description="Reload a Module")
@commands.has_role(845497466249412628)  # Samantha config man roles
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'<:check:839158727512293406> Reloaded **{extension}** module.')


@reload.error
async def reload_error(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=f"<:cross:839158779815657512> You must have the <@&845497466249412628> roles to use this command!")
        await ctx.channel.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@slash.slash(name="shutdown", description="Shutdowns the Bot.")
@commands.has_role(845497466249412628)  # Samantha config man roles
async def shutdown(ctx):
    await ctx.send(f':wave: The bot has been Shutdowned, Goodbye World.')
    channel = client.get_channel(831215570631393392)  # server-logs
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


@slash.slash(name="reboot", description="Reboot the Bot.")
@commands.has_role(845497466249412628)  # Samantha config man roles
async def reboot(ctx):
    await ctx.send(f':wave: The bot has been Rebooting, Please Wait..')
    channel = client.get_channel(831215570631393392)  # server-logs
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


@ client.event
async def on_ready():

    # versioning.

    version = ("main")

    # Turn this on/off if wanna go stable
    # version = ("main")
    # Turn this on/off if wanna go testing mode
    # version = ("testing")

    if version == "testing":
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name=version))
        channel = client.get_channel(864214499656466432)
        embed = discord.Embed(
            description=f"<a:WaveBlob:827337423649505300> Hey there, **Sam.py** initialised with version **{version}**", colour=discord.Colour.green())
        await channel.send(embed=embed)
        logging.basicConfig(level=logging.INFO)
        logging.basicConfig(level=logging.WARNING)
        logging.basicConfig(level=logging.ERROR)
        logging.basicConfig(level=logging.CRITICAL)
        logging.basicConfig(level=logging.DEBUG)

    if version == "main":
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=version))
        channel = client.get_channel(831215570631393392)
        embed = discord.Embed(
            description=f"<a:WaveBlob:827337423649505300> Hey there, **Sam.py** initialised with version **{version}**", colour=discord.Colour.green())
        await channel.send(embed=embed)

    print(f"Sam.py is ready with version {version}")

# sam normal token
client.run('insert your bot token here :)')

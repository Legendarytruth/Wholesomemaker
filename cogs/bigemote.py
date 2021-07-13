import os
import random
import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
import functools
import asyncio
import io


class bigemote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="bigemote",
                       description="Make a Emoji Bigger.",
                       options=[
                           create_option(
                               name="emoji",
                               description="Please Provide the Emoji.",
                               option_type=3,
                               required=True
                           )
                       ])
    async def bigemote(self, ctx: SlashContext, emoji):
        try:
            if emoji[0] == '<':
                name = emoji.split(':')[1]
                emoji_name = emoji.split(':')[2][:-1]
                anim = emoji.split(':')[0]
            if anim == '<a':
                url = f'https://cdn.discordapp.com/emojis/{emoji_name}.gif'
            else:
                url = f'https://cdn.discordapp.com/emojis/{emoji_name}.png'
            try:
                await ctx.send(url)
            except Exception as e:
                print(e)
                async with self.session.get(url) as resp:
                    if resp.status != 200:
                        er = "<:cross:839158779815657512> Error: Emote not found."
                        e = discord.Embed(title=er, color=discord.Color.red())
                        await ctx.send(embed=e)
                        return
                    img = await resp.read()

                kwargs = {'parent_width': 1024, 'parent_height': 1024}
                convert = False
                task = functools.partial(
                    bigemote.generate, img, convert, **kwargs)
                task = self.bot.loop.run_in_executor(None, task)
                try:
                    img = await asyncio.wait_for(task, timeout=15)
                except asyncio.TimeoutError:
                    er = "<:cross:839158779815657512> Error: Timed Out. Try again in a few seconds"
                    e = discord.Embed(title=er, color=discord.Color.red())
                    await ctx.send(embed=e)
                    return
                await ctx.send(file=discord.File(img, filename=name + '.png'))

        except Exception as e:
            er = "<:cross:839158779815657512> Error, couldn't send emote."
            e = discord.Embed(title=er, color=discord.Color.red())
            await ctx.send(embed=e)


@staticmethod
def generate(img, convert, **kwargs):
    img = io.BytesIO(img)
    return img


def setup(client):
    client.add_cog(bigemote(client))

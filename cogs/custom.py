import os
import random
import discord
from discord.ext import commands


class custom(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rules(self, ctx, *, member:  discord.Member = None):

        if member is None:
            member = ctx.author

        await ctx.message.delete()
        await ctx.send(f'Hey {member.mention}, {ctx.message.author.display_name} thinks you should take another look at our <#828959702029041664>')

    # put this on, if the server is not currently lockdowned.
    @commands.command()
    async def invite(self, ctx):
        await ctx.reply(f'https://discord.gg/HKjmPqJyre', mention_author=False)

    # put this on, if the server is currently lockdowned.
    # @commands.command()
    # async def invite(self, ctx, *, member:  discord.Member = None):
    #
    #    if member is None:
    #        member = ctx.author
    #
    #    await ctx.reply(f"Hey {member.mention}, I know you want the invite. but, It seems i don't have the invite. You should DM me or DM admin. Thanks.", mention_author=False)

    @commands.command()
    async def roles(self, ctx, *, member:  discord.Member = None):

        if member is None:
            member = ctx.author

        await ctx.reply(f'Hey {member.mention}, You can Assign/Resign your Roles by React on <#806958144404062229>', mention_author=False)

def setup(client):
    client.add_cog(custom(client))

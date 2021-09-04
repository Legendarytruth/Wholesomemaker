import os
import random
import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option


class avatar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="avatar",
                       description="See your or someone Avatar",
                       options=[
                           create_option(
                               name="member",
                               description="Who is the Person?",
                               option_type=6,
                               required=True
                           )])
    async def avatar(self, ctx: SlashContext, *, member):
        member = ctx.author if not member else member
        embed = discord.Embed(
            title=f"{member.display_name}'s avatar", color=member.color)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(avatar(client))

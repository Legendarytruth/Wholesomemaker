import os
import random
import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option


class unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="unban",
                       description="Unban a user.",
                       options=[
                           create_option(
                               name="id",
                               description="Who is the Person Should I Unban? (UserID Only)",
                               option_type=4,
                               required=True
                           )
                       ])
    @commands.has_role(845586428057354253)
    async def unban(self, ctx: SlashContext, id: int):
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        embed = discord.Embed(
            description=f"<:check:839158727512293406> Successfully unbanned {user.mention}")
        await ctx.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&845586428057354253> roles to use this command!")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(unban(client))

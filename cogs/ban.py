import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
from discord_slash import *
from discord_slash.utils.manage_commands import create_option


class ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="ban",
                       description="Ban a user.",
                       options=[
                           create_option(
                               name="user_id",
                               description="Who is the Person Should I Ban? (UserID Only)",
                               option_type=3,
                               required=True
                           ),
                           create_option(
                               name="reason",
                               description="Provide the Reason (Optional)",
                               option_type=3,
                               required=False
                           )
                       ])
    @commands.has_role(845586428057354253)
    async def ban(self, ctx: SlashContext, user_id, *, reason: Optional[str] = "No reason provided."):
        user = await self.client.fetch_user(user_id)
        try:
            await user.send(f'You have been banned from **{ctx.guild}** for the following reason: {reason}')
        except:
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> Failed to send DM to <@{user_id}>. They probably had their DM's closed.")
            await ctx.send(embed=embed)
        await ctx.guild.ban(user, reason=reason)
        embed = discord.Embed(
            description=f"<:check:839158727512293406> Successfully banned {user} for: {reason}")
        await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                description=f"<:cross:839158779815657512> You must have the <@&845586428057354253> roles to use this command!")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ban(client))

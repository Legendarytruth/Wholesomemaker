import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
from discord import Embed
from typing import Optional
import datetime
import asyncio


class serverinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="serverinfo", description="Provide you with this Server Info.")
    async def serverinfo(self, ctx: SlashContext):
        name = str(ctx.guild.name)
        owner = str(ctx.guild.owner_id)
        id = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)
        boostlevel = str(ctx.guild.premium_tier)
        woah = str(ctx.guild.created_at.strftime("%d/%m/%Y"))

        embed = discord.Embed(
            color=discord.Color.purple()
        )

        embed.set_author(
            name=f"{name}", icon_url=icon)
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=f'<@{owner}>', inline=True)
        embed.add_field(
            name="Region", value=f'{ctx.guild.region}', inline=True)
        embed.add_field(name="Categories",
                        value=f'{len(ctx.guild.categories)}', inline=True)
        embed.add_field(name="Text Channels",
                        value=f'{len(ctx.guild.text_channels)}', inline=True)
        embed.add_field(name="Voice Channels",
                        value=f'{len(ctx.guild.voice_channels)}', inline=True)
        embed.add_field(name="Members", value=memberCount, inline=True)
        embed.add_field(name="Roles",
                        value=f'{len(ctx.guild.roles)}', inline=True)
        embed.add_field(name="Boost Level", value=boostlevel, inline=True)
        embed.set_footer(
            text=f"ID : {id} | Server Created • {woah}")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(serverinfo(client))

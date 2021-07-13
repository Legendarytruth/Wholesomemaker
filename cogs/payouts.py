import os
import random
import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option


class payouts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="payouts", description="Provide you with some Cayo Perico Heist Loot Calculations.")
    async def payouts(self, ctx: SlashContext):
        await ctx.send(f'https://media.discordapp.net/attachments/689477347325509672/802101810974294016/secondaryloot.png')


def setup(client):
    client.add_cog(payouts(client))

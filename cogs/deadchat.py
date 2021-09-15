import os
import random
import discord
from discord.ext import commands


class deadchat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.guild_only()
    @commands.Cog.listener()
    async def on_message(self, ctx):
        kung = ('dead chat', 'deadchat', 'dchat', 'ded chat',
                'ded chat xd', 'dead chat xd', 'dedchat xd', 'deadchat xd', 'Dead сhat')
        if ctx.content.startswith(kung):
            await ctx.reply(f"If the chat is dead, it means that people have better things to do than keep it alive. How about you {ctx.author.display_name}? Why don't you keep it alive?", mention_author=False)


def setup(client):
    client.add_cog(deadchat(client))

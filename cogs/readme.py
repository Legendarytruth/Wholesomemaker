import discord
import discord_slash.cog_ext
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
from discord_slash.utils.manage_components import create_button, create_actionrow
from github import Github

load_dotenv()

client = Github(os.getenv("GITHUB_TOKEN"))
gist = client.get_gist(os.getenv("GIST_ID"))
first_file = list(gist.files.values())[0]
results = first_file.raw_data['content']


class readme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def readme(self, ctx):
        channel = self.client.get_channel(828959702029041664)
        await channel.send(results)


def setup(client):
    client.add_cog(readme(client))

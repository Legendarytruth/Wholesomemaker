import discord
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp
from discord_slash import *
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow


class role(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def toggleroles(self, ctx):
        if ctx.channel.id == 808958457855344640:
            role = discord.utils.get(
                ctx.guild.roles, name='youtube notifications')
            role1 = discord.utils.get(
                ctx.guild.roles, name='product users')
            role2 = discord.utils.get(
                ctx.guild.roles, name='tech news notifications')
            role3 = discord.utils.get(
                ctx.guild.roles, name='gta')
            await ctx.author.remove_roles(role)
            await ctx.author.remove_roles(role1)
            await ctx.author.remove_roles(role2)
            await ctx.author.remove_roles(role3)
            return await ctx.author.send(f"<:check:839158727512293406> **{ctx.author.display_name}**, You just Revoke All the Given Roles.")
        else:
            return await ctx.send(f"<:cross:839158779815657512> **{ctx.author.mention}**, that command is disabled in this channel.")

    @commands.command()
    @commands.is_owner()
    async def role(self, ctx):
        select = create_select(
            options=[  # the options in your dropdown
                create_select_option("Youtube", value="youtube", emoji="▶",
                                     description="Assign Youtube Notification role (Pingable)"),
                create_select_option("Product", value="product", emoji="🤖",
                                     description="Assign Product Updates role (Not Pingable)"),
                create_select_option("Tech News", value="technews", emoji="📰",
                                     description="Assign Tech News Notifications role (Pingable)"),
                create_select_option("Member", value="member", emoji="🧑",
                                     description="Assign Member role (Not Pingable)"),
                create_select_option(
                    "GTA", value="gta", emoji="🎮", description="Assign GTA role (Not Pingable)")
            ],
            # the placeholder text to show when no options have been chosen
            placeholder="Make a selection",
            min_values=1,
            max_values=1,  # the maximum number of options a user can select
        )
        channel = self.client.get_channel(806958144404062229)
        embed = discord.Embed(colour=discord.Colour.dark_green())
        embed.set_author(
            name='Role info:')
        embed.set_thumbnail(
            url="https://probot.media/8LBlJpkekY.png")
        embed.add_field(name='_ _',
                        value=f"<@&823029389154844743> - Owner of this server.", inline=False)
        embed.add_field(name='_ _',
                        value=f"<@&845586428057354253> - Basically, Head of ~~Moderators~~ <@&825578057498099732>", inline=False)
        embed.add_field(name='_ _',
                        value=f"<@&825578057498099732> - They are here to moderate the server and keeping this server up and running smoothly.", inline=False)
        embed.add_field(name='_ _',
                        value=f"<@&806950207240667147> - <@351147060956889088> Bot's (MatthewSoft Products)", inline=False)
        embed.add_field(name='_ _',
                        value=f"<@&807367008088883211> - Just Usual Server Bots", inline=False)
        embed.add_field(name='_ _',
                        value=f"<@&818231178070851636> - Consequences of ignoring the Rules, You'll Get this Role.", inline=False)
        embed.add_field(name='_ _',
                        value=f"<@&823145464831672331> - This role can be obtained by boosting the server. (Perks : Display above members, gets access to <#823152070189383700>, Custom role, and More to come).", inline=False)
        # embed.add_field(name='_ _',
        #                value=f"<@&812169490435014656> - <@351147060956889088> Close Friends. (Special Role, Not Obtainable)", inline=False)
        embed.add_field(name='_ _',
                        value=f"<@&834833966518370315> - Automatically given when you join the server.", inline=False)
        embed.add_field(name='_ _',
                        value=f"<@&817979175637352469> - This role will be given when you're verified by <@&823029389154844743> or <@&825578057498099732>.", inline=False)
        embed.add_field(name='_ _',
                        value=f"<@&808205557374517309> - <@351147060956889088> Youtube Channel Subscribers.", inline=False)
        embed.add_field(name='_ _',
                        value=f"<@&813398923099897886> - <@&806950207240667147> Bot Users.", inline=False)
        embed.add_field(name='_ _',
                        value=f"<@&825637144731058207> - Verified Members Access Pass to all {ctx.guild.name} Members Area.", inline=False)
        embed.set_footer(
            text=f"... and more, will you be able to find them all?", icon_url="https://probot.media/GPsmnC95sw.gif")
        # like action row with buttons but without * in front of the variable
        embed1 = discord.Embed(colour=discord.Colour.dark_green())
        embed1.set_author(
            name='Take your Role!')
        embed1.set_thumbnail(
            url="https://probot.media/8LBlJpkekY.png")
        embed1.add_field(name='_ _',
                         value=f"1. Choose `Youtube` to Assign the <@&808205557374517309> role (**Pingable**)", inline=False)
        embed1.add_field(name='_ _',
                         value=f"2. Choose `Product` to Assign the <@&813398923099897886> role (**Not Pingable**)", inline=False)
        embed1.add_field(name='_ _',
                         value=f"3. Choose `Tech News` to Assign the <@&831925045134884875> role (**Pingable**)", inline=False)
        embed1.add_field(name='_ _',
                         value=f"4. Choose `Member` to Assign the <@&825637144731058207> role (**Not Pingable**)", inline=False)
        embed1.add_field(name='_ _',
                         value=f"5. Choose `GTA` Assign the <@&881507994855153694> role (**Not Pingable**)", inline=False)
        embed1.set_footer(
            text=f"Pick a Option to get a role!", icon_url="https://probot.media/luV8g6k4WT.gif")
        await channel.send(embed=embed)
        await channel.send(embed=embed1)
        await channel.send(f"Pick your Preferred Roles using these Dropdowns!", components=[create_actionrow(select)])
        await channel.send(f"To Revoke ***Possible All Roles*** that already assigned to you, type the command `!toggleroles` on <#808958457855344640>. Thanks.")

    @commands.Cog.listener()
    async def on_component(self, ctx: ComponentContext):
        # ctx.selected_options is a list of all the values the user selected
        if ctx.selected_options[0] == "youtube":
            role = discord.utils.get(
                ctx.guild.roles, name='youtube notifications')
            await ctx.author.add_roles(role)
            return await ctx.send("You just Assign Youtube Notifications Role.", hidden=True)
        if ctx.selected_options[0] == "product":
            role = discord.utils.get(
                ctx.guild.roles, name='product users')
            await ctx.author.add_roles(role)
            return await ctx.send("You just Assign Product User Role.", hidden=True)
        if ctx.selected_options[0] == "technews":
            role = discord.utils.get(
                ctx.guild.roles, name='tech news notifications')
            await ctx.author.add_roles(role)
            return await ctx.send("You just Assign Tech News Notifications Role.", hidden=True)
        if ctx.selected_options[0] == "member":
            role = discord.utils.get(
                ctx.guild.roles, name='member')
            await ctx.author.add_roles(role)
            return await ctx.send("You just Assign Member Role.", hidden=True)
        if ctx.selected_options[0] == "gta":
            role = discord.utils.get(
                ctx.guild.roles, name='gta')
            await ctx.author.add_roles(role)
            return await ctx.send("You just Assign GTA Role.", hidden=True)


def setup(client):
    client.add_cog(role(client))

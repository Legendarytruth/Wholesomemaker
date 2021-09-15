import discord
from discord.ext import commands
from discord import Embed
from typing import Optional
import datetime
import asyncio
import aiohttp


class role(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def youtube(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='youtube notifications')
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** Has leave <@&808205557374517309> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)
        else:
            await ctx.author.add_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** Has joined <@&808205557374517309> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)

    @commands.command()
    async def product(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='product users')
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** Has leave <@&813398923099897886> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)
        else:
            await ctx.author.add_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** Has joined <@&813398923099897886> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)

    @commands.command()
    async def technews(self, ctx):
        role = discord.utils.get(
            ctx.guild.roles, name='tech news notifications')
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** Has leave <@&831925045134884875> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)
        else:
            await ctx.author.add_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** Has joined <@&831925045134884875> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)

    @commands.command()
    async def visitors(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='visitors')
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** Has leave <@&825637144731058207> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)
        else:
            await ctx.author.add_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** Has joined <@&825637144731058207> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)

    @commands.command()
    async def gta(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='GTA')
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** Has leave <@&881507994855153694> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)
        else:
            await ctx.author.add_roles(role)
            success = discord.Embed(
                description=f"<:check:839158727512293406> **{ctx.author.mention}** Has joined <@&881507994855153694> role", colour=discord.Colour.green())
            return await ctx.send(embed=success)


def setup(client):
    client.add_cog(role(client))

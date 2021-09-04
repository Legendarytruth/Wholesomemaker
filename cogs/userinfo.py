import os
import random
import discord
import discord_slash.cog_ext
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option


class userinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['ui'])
    async def userinfo(self, ctx, *, member: discord.Member = None):

        if member is None:
            member = ctx.author

        since_created = (ctx.message.created_at - member.created_at).days
        since_joined = (ctx.message.created_at - member.joined_at).days
        date_format = member.created_at.strftime("%a, %d %b %Y %I:%M %p")
        date_format2 = member.joined_at.strftime("%a, %d %b %Y %I:%M %p")
        created_on = f"{date_format}\n({since_created} days ago)"
        joined_at = f"{date_format2}\n({since_joined} days ago)"

        roles = list(
            reversed([x.name for x in member.roles if x.name != "@everyone"]))

        if roles:
            roles = "\n".join(roles)
        else:
            roles = "None"

        embed = discord.Embed(color=member.color)
        embed.set_author(name=str(member))
        developer = (351147060956889088)
        owner = ctx.guild.owner_id
        date_format = "%a, %d %b %Y %I:%M %p"
        embed.add_field(name=f"Joined Discord On:",
                        value=created_on, inline=False)
        embed.add_field(name=f"Joined Server At:",
                        value=joined_at, inline=False)
        #members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        if len(member.roles[1:]) < 1:
            embed.add_field(name=f"Roles:", value="None", inline=False)
            embed.add_field(name="User ID:",
                            value=f"{member.id}", inline=False)
            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        elif roles != None:
            embed.add_field(name="Roles:", value=", ".join([role.mention for role in list(
                reversed(member.roles)) if not role.is_default()]), inline=False)
            embed.add_field(name="User ID:",
                            value=f"{member.id}", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        if member.id == owner:
            embed.add_field(name='Acknowledgements',
                            value='Server Owner', inline=False)
        if member.id == developer:
            embed.add_field(
                name='Team', value='Bot Owner and Developer', inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def roleinfo(self, ctx, role: discord.Role):
        dd = ctx.guild.roles
        if role in dd:
            # timestamp=datetime.utcnow())
            embed = discord.Embed(title="Role Info", colour=role.color)
        fields = [("Name:", str(role), True),
                  ("ID:", role.id, True),
                  ("Color:", role.color, True),
                  ("Mentionable:", role.mentionable, True),
                  ("Position:", role.position, True),
                  ("Created at:", role.created_at.strftime("%a, %d %b %Y %I:%M %p"), True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(userinfo(client))

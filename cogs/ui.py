import os
import random
import discord
from discord.ext import commands


class ui(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['userinfo'])
    async def ui(self, ctx, *, member: discord.Member = None):

        if member is None:
            member = ctx.author

            since_created = (ctx.message.created_at - member.created_at).days
            since_joined = (ctx.message.created_at - member.joined_at).days
            member_created = member.created_at.strftime("%d %b %Y %H:%M")
            member_joined = member.joined_at.strftime("%d %b %Y %H:%M")

            created_on = f"{member_created}\n({since_created} days ago)"
            joined_at = f"{member_joined}\n({since_joined} days ago)"

            roles = list(
                reversed([x.name for x in member.roles if x.name != "@everyone"]))

        if roles:
            roles = "\n".join(roles)
        else:
            roles = "None"

        embed = discord.Embed(colour=0xffd300)
        embed.set_author(name=str(member))
        embed.add_field(name="Joined Discord on:",
                        value=created_on, inline=False)
        embed.add_field(name="Joined Server at: ",
                        value=joined_at, inline=False)
        embed.add_field(name="Roles:", value=", ".join([role.mention for role in list(
            reversed(member.roles)) if not role.is_default()]), inline=False)
        embed.add_field(name="User ID:", value=f"{member.id}", inline=True)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ui(client))

import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import has_permissions, MissingPermissions

class Ban(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self,ctx, member:discord.Member, *,modreason=None):
        if modreason==None:
            modreason="no reason"
        await ctx.guild.ban(member)
        embedkick=discord.Embed(title="Success!", color=discord.Color.random())
        embedkick.add_field(name="Banned:", value=f"{member} has been banned by {ctx.author.mention}", inline=False)
        embedkick.add_field(name="Reason:", value=f"{modreason}", inline=False)
        await ctx.send(embed=embedkick)
    
async def setup(client):
    await client.add_cog(Ban(client))
import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import has_permissions, MissingPermissions

class Kick(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command(aliases=["hata","gu"])
    @has_permissions(kick_members=True)
    async def kick(self,ctx, member:discord.Member, *,modreason=None):
        if modreason==None:
            modreason="no reason"
        await ctx.guild.kick(member)
        embedkick=discord.Embed(title="Success!", color=discord.Color.random())
        embedkick.add_field(name="Kicked:", value=f"{member} has been kicked by {ctx.author.mention}", inline=False)
        embedkick.add_field(name="Reason:", value=f"{modreason}", inline=False)
        await ctx.send(embed=embedkick)
    
async def setup(client):
    await client.add_cog(Kick(client))
    
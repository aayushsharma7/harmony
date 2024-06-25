import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import has_permissions, MissingPermissions

class Avatar(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command(aliases=["pfp","av"])
    async def avatar(self,ctx, member:discord.Member):
        emb=discord.Embed(title="Avatar", color=discord.Color.random())
        emb.set_author(name=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)
        emb.set_image(url=member.avatar)
        await ctx.send(embed=emb)


   
    
async def setup(client):
    await client.add_cog(Avatar(client))
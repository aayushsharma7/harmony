import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import has_permissions, MissingPermissions

class Unban(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self,ctx, userID):
        user=discord.Object(id=userID)
        await ctx.guild.unban(user)
        embedkick=discord.Embed(title="Success!", color=discord.Color.random())
        embedkick.add_field(name="Unbanned:", value=f"<@{userID}> has been unbanned by {ctx.author.mention}", inline=False)
        await ctx.send(embed=embedkick)
   
        
    
async def setup(client):
    await client.add_cog(Unban(client))
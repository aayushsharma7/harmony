import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import has_permissions, MissingPermissions

class Hi(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command(aliases=["hi","hello","yo"])
    async def hey(self,ctx):
        await ctx.send("hey!")

async def setup(client):
    await client.add_cog(Hi(client))
    
    
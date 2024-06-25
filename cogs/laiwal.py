import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import has_permissions, MissingPermissions

class Laiwal(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command(aliases=["level","lvl"])
    async def laiwal(self,ctx):
        await ctx.send("accha laiwal nikalega?")    



async def setup(client):
    await client.add_cog(Laiwal(client))



    
import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import has_permissions, MissingPermissions

class Clear(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command(aliases=["purge"])
    @has_permissions(manage_messages=True)
    async def clear(self,ctx, *, count:int):
        if count>=100:
            await ctx.send("Limit is upto 100 only")
        elif count<=1:
            await ctx.send("Cannot remove less than 1 message")
        else:
            await ctx.channel.purge(limit=count)
            await ctx.send(f"{count} message(s) have been deleted")



async def setup(client):
    await client.add_cog(Clear(client))
    
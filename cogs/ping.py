import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")
    @commands.command(aliases=["latency"])
    async def ping(self,ctx):
        latency=round(self.client.latency * 1000)
        await ctx.send(f"{latency} ms")

async def setup(client):
    await client.add_cog(Ping(client))
    
    





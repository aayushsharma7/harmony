import discord
from discord.ext import commands, tasks
from itertools import cycle
import random

client = commands.Bot(command_prefix="-", intents=discord.Intents.all())
status=cycle(["Under Development"])

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
@client.event

async def on_ready():
    print("bot is connected to discord")
    change_status.start()

@client.command(aliases=["level"])
async def laiwal(ctx):
    await ctx.send("accha laiwal nikalega?")

@client.command(aliases=["hi","hello"])
async def hey(ctx):
    await ctx.send("hey!")

@client.command()
async def list(ctx):
    await ctx.send("List of Commands is -hey,-laiwal,-list,-ping")

@client.command()
async def ping(ctx):
    latency=round(client.latency * 1000)
    await ctx.send(f"{latency} ms")

@client.command(aliases=["8ball"])
async def ask(ctx, *, question):
    with open("bot/resp.txt", "r") as f:
        resp=f.readlines()
        response=random.choice(resp)
    await ctx.send(response)
    
    
client.run("MTI0NDY4MzgzMjcwNDIzNzYyOA.GVB5PO.u28X-lHlZZNySw2ltF03vk5NzhiBroklk3-WNQ")
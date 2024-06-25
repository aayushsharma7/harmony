import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import has_permissions, MissingPermissions
import os
import asyncio

client = commands.Bot(command_prefix="-", intents=discord.Intents.all())
status=cycle(["Under Development"])

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
@client.event

async def on_ready():
    print("bot is connected to discord")
    change_status.start()

@client.remove_command("help")

@client.command()
async def help(ctx):
    hel=discord.Embed(title="Help", description="All commands available are listed here", color=discord.Color.random())
    hel.set_author(name="Harmony", icon_url=client.user.avatar)
    hel.add_field(name="Clear/Purge",value="Deletes a specified amount of messages", inline=False)
    hel.add_field(name="Ping/Latency",value="Gives user's latency", inline=False)
    hel.add_field(name="Avatar/Av/Pfp",value="Displays the mentioned user's profile picture", inline=False)
    hel.add_field(name="Kick",value="Kicks the mentioned user from the server", inline=False)
    hel.add_field(name="Ban",value="Bans the mentioned user from the server", inline=False)
    hel.add_field(name="Unban",value="Unbans the mentioned user from the server", inline=False)
    hel.add_field(name="Need Help?",value="[Join the support server!](https://discord.gg/wpXzG9d2)", inline=False)
    await ctx.send(embed=hel)

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send("kya hai gadhe, bt na de, hehe")
    await client.process_commands(message)

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send("Use -help for further information!")
    if 'bhalu' in message.content:
        await message.channel.send("chotu")
    await client.process_commands(message)

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start("MTI0NDY4MzgzMjcwNDIzNzYyOA.GVB5PO.u28X-lHlZZNySw2ltF03vk5NzhiBroklk3-WNQ")

asyncio.run(main())
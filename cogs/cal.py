import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import has_permissions, MissingPermissions

class Cal(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command(aliases=["calc","calculate"])
    async def cal(self,ctx, *, expression:str):
        if "+" in expression:
            p=int(expression.find("+"))
            l=len(expression)
            numone=int(expression[0:p])
            numtwo=int(expression[p+1:l])
            ope=numone+numtwo
            solve=discord.Embed(title="Calculator", color=discord.Color.random())
            solve.add_field(name="Input", value=f"`{numone}+{numtwo}`",inline=False)
            solve.add_field(name="Output", value=f"`{ope}`",inline=False)
            await ctx.send(embed=solve)


        elif "-" in expression:
            p=int(expression.find("-"))
            l=len(expression)
            numone=int(expression[0:p])
            numtwo=int(expression[p+1:l])
            ope=numone-numtwo
            solve=discord.Embed(title="Calculator", color=discord.Color.random())
            solve.add_field(name="Input", value=f"`{numone}-{numtwo}`",inline=False)
            solve.add_field(name="Output", value=f"`{ope}`",inline=False)
            await ctx.send(embed=solve)
                       
        elif "*" in expression:
            p=int(expression.find("*"))
            l=len(expression)
            numone=int(expression[0:p])
            numtwo=int(expression[p+1:l])
            ope=numone*numtwo
            solve=discord.Embed(title="Calculator", color=discord.Color.random())
            solve.add_field(name="Input", value=f"`{numone}*{numtwo}`",inline=False)
            solve.add_field(name="Output", value=f"`{ope}`",inline=False)
            await ctx.send(embed=solve)
                       
        elif "/" in expression:
            p=int(expression.find("/"))
            l=len(expression)
            numone=int(expression[0:p])
            numtwo=int(expression[p+1:l])
            ope=numone/numtwo
            solve=discord.Embed(title="Calculator", color=discord.Color.random())
            solve.add_field(name="Input", value=f"`{numone}/{numtwo}`",inline=False)
            solve.add_field(name="Output", value=f"`{ope}`",inline=False)
            await ctx.send(embed=solve)
                       
        elif "t" in expression:
            p=int(expression.find("t"))
            l=len(expression)
            numone=int(expression[0:p])
            numtwo=int(expression[p+1:l])
            ope=numone**numtwo
            solve=discord.Embed(title="Calculator", color=discord.Color.random())
            solve.add_field(name="Input", value=f"`{numone}**{numtwo}`",inline=False)
            solve.add_field(name="Output", value=f"`{ope}`",inline=False)
            await ctx.send(embed=solve)
                       

        
async def setup(client):
    await client.add_cog(Cal(client))
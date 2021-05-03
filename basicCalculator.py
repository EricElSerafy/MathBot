import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '?')

@bot.command()
async def ping(context):
    await context.send(f'{round(bot.latency*1000)} ms')
    print('hi')

@bot.command('calc')
async def calculate(context, *, problem):
    await context.send(f'Problem: {problem}\nAnswer: {eval(problem)}') 
    
    
bot.run('ODM4NTQ3NjU0OTU0ODQ0MTkw.YI8sXA.UTF8HLgq4bUfaA_-5C4iND9MTuM')
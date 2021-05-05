from apiKey import apiKey
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '?')

@bot.command()
async def ping(context):
    await context.send(f'{round(bot.latency*1000)} ms')
    print('hi')



@bot.command('calc')
async def calculate(context, *, problem):
    if '^' in problem:
        await context.send(f'Problem: {problem}')
        problem = problem.replace('^', '**')     
        await context.send(f'Answer: {eval(problem)}') 
    

bot.run(apiKey)
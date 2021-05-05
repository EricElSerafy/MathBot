import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '?')

@bot.command()
async def ping(context):
    await context.send(f'{round(bot.latency*1000)} ms')
    print('hi')

# prob = '2^3'
# prob.replace

@bot.command('calc')
async def calculate(context, *, problem):
    if '^' in problem:
        await context.send(f'Problem: {problem}')
        problem = problem.replace('^', '**')   
        print(problem)
        
        await context.send(f'Answer: {eval(problem)}') 
    
    
bot.run('ODM4NTQ3NjU0OTU0ODQ0MTkw.YI8sXA.UTF8HLgq4bUfaA_-5C4iND9MTuM')